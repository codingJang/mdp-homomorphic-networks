#!/bin/bash

# Run 50 seeds with the best-performing learning rate for each network
for c in {0..4}
do
	for i in {0..2}
	do
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 8 8  --const 0.09 &
		sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 8 8  --const 0.18 &
		sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 16 16  --const 0.04 &
		sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 16 16  --const 0.08 &
		sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 32 32  --const 0.018 &
		sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 32 32  --const 0.036 &
		sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 64 64  --const 0.008 &
		sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 64 64  --const 0.016 &
		sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 128 128  --const 0.004 &
		sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 128 128  --const 0.008 &
		sleep 1
	done
	wait
done
