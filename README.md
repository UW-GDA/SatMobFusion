# SatMobFusion

##  A novel real-time event-identification methodology fusing satellite imagery with mobile sensor data

Rapid identification of breaking events and percolation of relevant information is of paramount importance, especially during life-threatening events like natural disasters. The prevalence of mobile devices and the ubiquity of network connectivity has generated a massive amount of temporally- and spatially-stamped data (called mobile data hereafter). Numerous studies have used mobile data to derive individual human mobility patterns for various applications (Gonzalez et al., 2008; Sulis et al., 2018; Edsberg Møllgaard et al., 2022). Similarly, the increasing number of orbital satellites has made it easier to gather high-resolution images capturing a snapshot of a geographical area in sub-daily temporal frequency (Ji et al., 2018, Fayne et al., 2016). We propose a novel data fusion methodology integrating satellite imagery with mobile data to identify breaking events in real-time. In the absence of boots on the ground, mobile data is able to give an approximation of human mobility, proximity to one another, and the built environment. On the other hand, satellite imagery can provide real-time visual information on physical changes to the built and natural environment. Our goal is to prototype a methodology that could be used in disaster relief when sufficient resources are available to pull together sub-daily, near real-time data to input in our framework.

**Objective**: Assess the extent to which high-resolution satellite imagery is a feasible alterantive or supplement to more established transportation data collection methods, such as cameras, crowdsourcing, and vehicle counters.

**Datasets**: 
* [Spectus Data](https://spectus.ai/): Passively-generated mobile data
* [Planet Data](https://www.planet.com/): High-resolution, high frequency satellite imagery

**Tools/packages**
* [Scikit Mobility](https://github.com/scikit-mobility/scikit-mobility): Library for human mobility analysis in Python
* [mobileDataToolkit](https://github.com/ekinugurel/mobileDataToolKit): Personal collection of convenience functions/ML tools for human mobility analysis
* [GeoPandas](https://geopandas.org/en/stable/): Library for geospatial data analysis in Python
* [Rasterio](https://rasterio.readthedocs.io/en/latest/intro.html): Raster data library for Python

### Methodology
After receiving access to satellite data, we plan on doing extensive data cleaning and analysis to see what type of events we can identify and match using both of our data sources across different geographies. Once we settle on a few events that we feel confident about going forward with, we plan on designing a simulation study of each event. This study would replicate the real-time availability of each dataset to gain an understanding of whether our proposed methodology leads to improvements in relevant variables, including emergency response times, information percolation speeds, etc. We expect to dig deeper into the context of our selected events, such as finding out about the availability of other data sources and the actual response time in order to benchmark our findings.

### Expected Outcomes
Our proposed methodology is expected to outperform existing methods for data collection and information percolation for a range of use cases. We especially anticipate broad applicability in the following settings: events in rural areas, war-torn states, areas without network connectivity (i.e., for crowdsourcing), and national security matters.

### References
* González, M.C., Hidalgo, C.A., Barabási, A.-L., 2008. Understanding individual human mobility patterns. Nature 453, 779–782. https://doi.org/10.1038/nature06958
* Sulis, P., Manley, E., Zhong, C., Batty, M., 2018. Using mobility data as proxy for measuring urban vitality. Journal of Spatial Information Science 2018, 137–162. https://doi.org/10.5311/JOSIS.2018.16.384
* Edsberg Møllgaard, P., Lehmann, S., Alessandretti, L., 2021. Understanding components of mobility during the COVID-19 pandemic. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 380, 20210118. https://doi.org/10.1098/rsta.2021.0118
* Ji, M., Liu, L., Buchroithner, M., 2018. Identifying Collapsed Buildings Using Post-Earthquake Satellite Imagery and Convolutional Neural Networks: A Case Study of the 2010 Haiti Earthquake. Remote Sensing 10, 1689. https://doi.org/10.3390/rs10111689
* Fayne, J., Bolten, J., Lakshmi, V., Ahamed, A., 2017. Optical and Physical Methods for Mapping Flooding with Satellite Imagery, in: Lakshmi, V. (Ed.), Remote Sensing of Hydrological Extremes, Springer Remote Sensing/Photogrammetry. Springer International Publishing, Cham, pp. 83–103. https://doi.org/10.1007/978-3-319-43744-6_5

