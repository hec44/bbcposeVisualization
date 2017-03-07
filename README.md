# bbcposeVisualization
The porpose of this repo is to use [bbc pose dataset](https://www.robots.ox.ac.uk/~vgg/data/pose/index.html#downloadlink) in other leanguages, like python.

Simple matlab and python code to transform bbcpose joints anotation to csv file and visualization in python with opencv
First, download dataset, can be downloaded [here](https://www.robots.ox.ac.uk/~vgg/data/pose/index.html#downloadlink)
Usage:
In matlab:
  struct2csv(structfile,csvPath)
  eg:
    structu2csv('shortbbcpose.mat','.')
Once having csv file with joints and frame information run python code

  python testimages.py
  
Then you should start looking at joints in the dataset
