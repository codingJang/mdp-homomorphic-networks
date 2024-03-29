"""
"""
from rlpyt.samplers.serial.sampler import SerialSampler
from rlpyt.samplers.parallel.cpu.sampler import CpuSampler
from rlpyt.samplers.parallel.gpu.sampler import GpuSampler
from rlpyt.samplers.parallel.gpu.alternating_sampler import AlternatingSampler
from rlpyt.envs.gym import make as gym_make
from rlpyt.algos.pg.a2c import A2C
from rlpyt.runners.minibatch_rl import MinibatchRlEval, MinibatchRl
from rlpyt.utils.logging.context import logger_context

from rlpyt.agents.pg.grid import GridBasisAgent   #EDIT# GridBasisAgent import하기

from ops import get_agent_cls_grid


def build_and_train(env_id="GridEnv-v1", run_ID=0, cuda_idx=None,
                    sample_mode="serial", n_parallel=2, args={}):
    affinity = dict(cuda_idx=cuda_idx, workers_cpus=list(range(n_parallel)))
    gpu_cpu = "CPU" if cuda_idx is None else f"GPU {cuda_idx}"
    if sample_mode == "serial":
        Sampler = SerialSampler  # (Ignores workers_cpus.)
        print(f"Using serial sampler, {gpu_cpu} for sampling and optimizing.")
    elif sample_mode == "cpu":
        Sampler = CpuSampler
        print(f"Using CPU parallel sampler (agent in workers), {gpu_cpu} for optimizing.")
    elif sample_mode == "gpu":
        Sampler = GpuSampler
        print(f"Using GPU parallel sampler (agent in master), {gpu_cpu} for sampling and optimizing.")
    elif sample_mode == "alternating":
        Sampler = AlternatingSampler
        affinity["workers_cpus"] += affinity["workers_cpus"]  # (Double list)
        affinity["alternating"] = True  # Sampler will check for this.
        print(f"Using Alternating GPU parallel sampler, {gpu_cpu} for sampling and optimizing.")


    sampler = Sampler(
        EnvCls=gym_make,
        env_kwargs=dict(id=env_id, stochastic=True, p=0.15, size=(7, 7)),
        batch_T=5,  # 5 time-steps per sampler iteration.
        batch_B=16,
        max_decorrelation_steps=1000,
        eval_n_envs=0,
    )


    algo = A2C(learning_rate=args.lr)

    agentCls, agent_basis = get_agent_cls_grid(args.network)
    if agentCls is GridBasisAgent:   #EDIT# 만약 에이전트 클래스가 GridBasisAgent라면, 객체 생성 시 키워드 인자에 args.const를 추가함
        agent = agentCls(model_kwargs={'basis': agent_basis,
                                    'channels': args.channels,
                                    'kernel_sizes': args.filters,
                                    'paddings': args.paddings,
                                    'fc_sizes': args.fcs,
                                    'strides': args.strides,
                                    'const': args.const,
                                    'cconst': args.cconst})
    else:
        agent = agentCls(model_kwargs={'basis': agent_basis,
                                    'channels': args.channels,
                                    'kernel_sizes': args.filters,
                                    'paddings': args.paddings,
                                    'fc_sizes': args.fcs,
                                    'strides': args.strides})
    runner = MinibatchRl(
        algo=algo,
        agent=agent,
        sampler=sampler,
        n_steps=2e6,
        log_interval_steps=10e3,
        affinity=affinity,
    )


    config = dict(env_id=env_id, lr=args.lr, network=args.network,
                  fcs=str(args.fcs), channels=args.channels,
                  strides=args.strides, paddings=args.paddings, const=args.const, cconst=args.const)  #EDIT# const 추가
    if agentCls is GridBasisAgent:  #EDIT# 만약 에이전트 클래스가 GridBasisAgent라면, 제목과 log_dir에 args.const를 추가함
        name = f"{args.folder}_{args.network}_{str(args.fcs).replace(' ', '')}_{str(args.filters).replace(' ', '')}_{args.const}_{args.cconst}"
        log_dir = f"{args.folder}_{args.network}_{str(args.fcs).replace(' ', '')}_{str(args.filters).replace(' ', '')}_{args.const}_{args.cconst}"
        # breakpoint()
    else:
        name = f"{args.folder}_{args.network}"
        log_dir = f"{args.folder}_{args.network}"
    with logger_context(log_dir, run_ID, name, config):
        runner.train()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--folder', help='Folder to store results',
                        default='GridworldExperiment')
    parser.add_argument('--env_id', help='Grid', default='GridEnv-v1')
    parser.add_argument('--lr', help='Learning rate', default=0.001, type=float)
    parser.add_argument('--network', help='network type',
                        default='equivariant', type=str)
    parser.add_argument('--fcs', type=int, nargs='+', default=[512])
    parser.add_argument('--channels', type=int, nargs='+', default=[16, 32])
    parser.add_argument('--filters',  type=int, nargs='+', default=[7, 5])
    parser.add_argument('--strides', type=int, nargs='+', default=[2, 1])
    parser.add_argument('--paddings', type=int, nargs='+', default=[0, 0])
    parser.add_argument('--run_ID', help='run identifier (logging)', type=int, default=0)
    parser.add_argument('--cuda_idx', help='gpu to use ', type=int, default=None)
    parser.add_argument('--sample_mode', help='serial or parallel sampling',
                        type=str, default='serial', choices=['serial', 'cpu', 'gpu', 'alternating'])
    parser.add_argument('--n_parallel', help='number of sampler workers', type=int, default=2)
    parser.add_argument('--const', help='const in num_samples = const*num_param/group_size', default=2.0, type=float)   #EDIT# const 인자 추가
    parser.add_argument('--cconst', help='cconst for convolutional layers', default=2.0, type=float)
    args = parser.parse_args()
    build_and_train(
        env_id=args.env_id,
        run_ID=args.run_ID,
        cuda_idx=args.cuda_idx,
        sample_mode=args.sample_mode,
        n_parallel=args.n_parallel, args=args
    )
