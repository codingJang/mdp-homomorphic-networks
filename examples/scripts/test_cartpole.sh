#!/bin/bash

# Run 50 seeds with the best-performing learning rate for each network
for c in {0..4}
do
	for i in {0..9}
	do
		# python cartpole_ppo.py --cuda_idx 0 --run_ID $((5*$c+$i)) --network equivariant --lr 0.01 --fcs 16 16  --const 0.06 &
		# sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 2 2  --const 1 &
		sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 2 2  --const 0.641 &
		sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 4 4  --const 0.214 &
		sleep 1
		python cartpole_ppo.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.01 --fcs 8 8  --const 0.0916 &
		sleep 1
	done
	wait
done
