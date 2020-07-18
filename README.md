# Diploma Project

## Intro

The script used in the project is available as a .py file in the repository. The script is also divided into three parts according to the dataset being used. Small changes can be made to the varaibles according to the process being used. Three input datasets used in the project are:

1. A self generated point cloud via structure through motion. The files are available with the name electrical pole and a subsequent cropped point cloud also, which was generated in the process

2. Two scans for ITC building Enschede for understanding manuel registration. The sample format is available to understand the structure of the input file into the open3d.

3. Benchmark dataset used in [3] The whole reconstruction pipeline is available at the github repository for the open3d. The implementation is very stright-forward. Link to the dataset and repository: http://redwood-data.org/indoor/ , https://github.com/intel-isl/Open3D

## Outline Objectives

Following is the list of objectives completed see the outline.md file
- [x] Reading different formats: polygon files, text files and rgbd images
- [x] Visualization: of all formats
- [x] Pre Processing: downsampling, outlier removal
- [x] Co-Registration of two points clouds: itc building scans

### Additional Objectives
- [ ] Understanding the Tensorflow implementation for semantic segmentation of point clouds
- [ ] More on structure from motion

## References*

[1]Song, S., Lichtenberg, S. P., & Xiao, J. (2015). SUN RGB-D: A RGB-D scene understanding benchmark suite. 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 567–576. https://doi.org/10.1109/CVPR.2015.7298655

[2]Sturm, J., Engelhard, N., Endres, F., Burgard, W., & Cremers, D. (2012). A benchmark for the evaluation of RGB-D SLAM systems. 2012 IEEE/RSJ International Conference on Intelligent Robots and Systems, 573–580. https://doi.org/10.1109/IROS.2012.6385773

[3]Sungjoon Choi, Zhou, Q.-Y., & Koltun, V. (2015). Robust reconstruction of indoor scenes. 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 5556–5565. https://doi.org/10.1109/CVPR.2015.7299195

[4]Zhou, Q.-Y., Park, J., & Koltun, V. (2018). Open3D: A Modern Library for 3D Data Processing. https://arxiv.org/abs/1801.09847v1

*Would like to thank all the contributors and the authors. The reference list non-exhaustive and would be updated throughout the work.
