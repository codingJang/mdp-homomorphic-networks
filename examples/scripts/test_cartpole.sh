#!/bin/bash

# Run 25 seeds with the best-performing learning rate for each network
for c in {0..0}
do
	for i in {0..4}
	do
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((5*$c+$i)) --network equivariant --lr 0.01 --fcs 32 32 --const 0.005 &
		sleep 4
		# python cartpole_ppo.py --cuda_idx 0 --run_ID $((5*$c+$i)) --network equivariant --lr 0.01 --fcs 32 32 --const 2.0 &
		# sleep 4
		# python cartpole_ppo.py --cuda_idx 0 --run_ID $((5*$c+$i)) --network equivariant --lr 0.01 --fcs 32 32 --const 1.0 &
		# sleep 4
		# python cartpole_ppo.py --cuda_idx 0 --run_ID $((5*$c+$i)) --network equivariant --lr 0.01 --fcs 32 32 --const 0.5 &
		# sleep 4
		# python cartpole_ppo.py --cuda_idx 0 --run_ID $((5*$c+$i)) --network equivariant --lr 0.01 --fcs 32 32 --const 0.25 &
		# sleep 4
	done
	# wait
done