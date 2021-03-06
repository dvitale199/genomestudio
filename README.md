# genomestudio
A few methods of using Illumina's Genome Studio for genotype calling

# Run with docker
#### docker image can be built as follows
```
cd docker
docker build --tag genomestudio .
```

#### Now with docker image, run on local idats, cluster, and manifest files
`docker run --rm -v <local data dir>:/mnt genomestudio /home/iaap-cli-linux-x64-1.1.0-sha.80d7e5b3d9c1fdfc2e99b472a90652fd3848bbc7/iaap-cli/iaap-cli gencall /mnt/Manifest_cluster_files/GSA-24v3-0_A2.bpm /mnt/Manifest_cluster_files/GSA-24v3-0_A1_ClusterFile.egt /mnt/output -f /mnt/204118120034/ -p`

where `<local data dir>` is a local directory containing all idats, cluster and manifest files.

#### gencall works as follows:
`/home/iaap-cli-linux-x64-1.1.0-sha.80d7e5b3d9c1fdfc2e99b472a90652fd3848bbc7/iaap-cli/iaap-cli gencall <manifest (.bpm)> <clusterfile (.egt)> <output dir> -f <path/to/idats/> -p` 

`-p` to make .ped output used in this run. (use `-g` to make .gtc output)

`--rm` removes container after run is complete

`-v` creates a volume with local dir mounted to /mnt in docker container (I chose to mount volume to /mnt but you could do this in any dir inside the container that you like).

#### Docker Example
`docker run --rm -v /Users/vitaled2/Desktop/genome_studio/ilmnTestData:/mnt genomestudio /home/iaap-cli-linux-x64-1.1.0-sha.80d7e5b3d9c1fdfc2e99b472a90652fd3848bbc7/iaap-cli/iaap-cli gencall /mnt/Manifest_cluster_files/GSA-24v3-0_A2.bpm /mnt/Manifest_cluster_files/GSA-24v3-0_A1_ClusterFile.egt /mnt/output -f /mnt/204118120034/ -p`

# Local Genome Studio CLI Parallel processing python script
#### This parallelizes runs for different sets of idats with same cluster/manifest
#### Run like this:

`python3 genome_studio_multi_caller.py --idats /data/vitaled2/genomestudio/idat_paths.txt \
--egt /data/vitaled2/genomestudio/GSAv3Demo/Manifest_cluster_files/GSA-24v3-0_A1_ClusterFile.egt \
--bpm /data/vitaled2/genomestudio/GSAv3Demo/Manifest_cluster_files/GSA-24v3-0_A2.bpm \
--out /data/vitaled2/genomestudio/output`

#### idat_paths.txt is just a text file with a different path to different sets of idats (must be from same chip-- i.e. same manifest and clusterfile). it looks like this:
```
/path/to/idats1/
/path/to/idats2/
```


