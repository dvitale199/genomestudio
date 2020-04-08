docker build --tag genomestudio .

docker run --rm -v /Users/vitaled2/Desktop/genome_studio/ilmnTestData:/mnt genomestudio /home/iaap-cli-linux-x64-1.1.0-sha.80d7e5b3d9c1fdfc2e99b472a90652fd3848bbc7/iaap-cli/iaap-cli gencall /mnt/Manifest_cluster_files/GSA-24v3-0_A2.bpm /mnt/Manifest_cluster_files/GSA-24v3-0_A1_ClusterFile.egt /mnt/output -f /mnt/204118120034/ -p

