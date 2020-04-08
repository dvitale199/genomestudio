# genomestudio
A few methods of using Illumina's Genome Studio for genotype calling

## Run with docker
#### docker image can be build as follows
```cd docker
docker build --tag genomestudio .
```

#### Now with docker image, run on local idats, cluster, and manifest files
`docker run --rm -v <local data dir>:/mnt genomestudio /home/iaap-cli-linux-x64-1.1.0-sha.80d7e5b3d9c1fdfc2e99b472a90652fd3848bbc7/iaap-cli/iaap-cli gencall /mnt/Manifest_cluster_files/GSA-24v3-0_A2.bpm /mnt/Manifest_cluster_files/GSA-24v3-0_A1_ClusterFile.egt /mnt/output -f /mnt/204118120034/ -p`
where `<local data dir>` is a local directory containing all idats, cluster and manifest files.

#### gencall works as follows:
`/home/iaap-cli-linux-x64-1.1.0-sha.80d7e5b3d9c1fdfc2e99b472a90652fd3848bbc7/iaap-cli/iaap-cli gencall <manifest (.bpm)> <clusterfile (.egt)> <output dir> -f <path/to/idats/> -p` 
`-p` to make .ped output used in this run. use <-g> to make .gtc output
`--rm` removes container after run is complete
`-v` creates a volume with local dir mounted to /mnt in docker container (I chose to mount volume to /mnt but you could do this in any dir inside the container that you like).

#### Docker Example
`docker run --rm -v /Users/vitaled2/Desktop/genome_studio/ilmnTestData:/mnt genomestudio /home/iaap-cli-linux-x64-1.1.0-sha.80d7e5b3d9c1fdfc2e99b472a90652fd3848bbc7/iaap-cli/iaap-cli gencall /mnt/Manifest_cluster_files/GSA-24v3-0_A2.bpm /mnt/Manifest_cluster_files/GSA-24v3-0_A1_ClusterFile.egt /mnt/output -f /mnt/204118120034/ -p`



