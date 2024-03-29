#!/bin/bash

# Run 20 seeds with the best-performing learning rate for each network
for c in {0..4}
do
	for i in {0..3}
	do
		# python grid_a2c.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.001 --const 0.1 --cconst 0.1 &
		# sleep 1
		# python grid_a2c.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.001 --const 0.01 --cconst 0.1 &
		# sleep 1
		# python grid_a2c.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.001 --const 0.001 --cconst 0.1 &
		# sleep 1
		python grid_a2c.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.001 --const 0.0003 --cconst 0.1 &
		sleep 1
		python grid_a2c.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.001 --const 0.0001 --cconst 0.1 &
		sleep 1
		python grid_a2c.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.001 --const 0.001 --cconst 0.03 &
		sleep 1
		python grid_a2c.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.001 --const 0.001 --cconst 0.001 &
		sleep 1
		python grid_a2c.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.001 --const 0.003 --cconst 0.03 &
		sleep 1
		python grid_a2c.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.001 --const 0.003 --cconst 0.001 &
		sleep 1
		python grid_a2c.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.001 --const 0.0001 --cconst 0.03 &
		sleep 1
		python grid_a2c.py --cuda_idx 0 --run_ID $((10*$c+$i)) --network equivariant --lr 0.001 --const 0.0001 --cconst 0.001 &
		sleep 1
	done
	wait
done

