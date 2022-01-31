Look up who is using the GPU
```bash
squeue --start -u $USER
(Current Users: pli081, jyang239, yliu807, sren, blu029)
```

Run slurm script: 
```bash
sbatch SBATCH_SCRIPT.sh
```

Interactive command:
```bash
srun -p gpu --gres=gpu:1 --mem=100g --time=1:00:00 --pty bash -l
```

Example SLURM scripts
```bash
#!/bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=10G
#SBATCH --time=2-00:00:00     # 1 day and 15 minutes
#SBATCH --mail-user=pli081@ucr.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name="exp_l3_0.4"
#SBATCH --gres=gpu:1
#SBATCH -p gpu # This is the default partition, you can use any of the following; intel, batch, highmem, gpu
```


