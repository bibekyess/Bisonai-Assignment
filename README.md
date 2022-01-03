**Application Link:** https://bisonai-task.herokuapp.com/ <br>
**Content Description** <br>
* Raw data folder contains the data source<br>
* static/styles contains the css file source<Br>
* templates contain the html file source<br>
* app.py is the main python file source<br>
* Processed data folder contains the data used in plotting the plots<br>
* Data_PreProcessing.ipynb is the colab notebook used in creating the dataset for plotting<br>
* Procfile and requirements.txt are the files used in deploying the application<br>

**Generating Data**<br>
I made use of google colab notebook to generate the false data. You can find the data used in 'Raw data' folder (single source is used). Then again using, google colab, I did data preprocessing and downloaded 4 datasets for plotting our desired graphs. Since, I just needed fake data, for TVL, I used sum() and for Volume 24H, I used average() of data values.<br>

**Passing data:**<br>
I have used flask to make the server and used python to fetch the data and then pass it to html file. Doing this, in future, if any preprocessing, is still required then one can easily do it using python.

**Line chart:**<br>
For line chart, we only require 1 dataset. Firstly, I appended svg element to the specified drawing position on html and then made x and y scales and appended each axes to the svg element. I wanted to color the area below the graph so I used d3.area() and I used gradient color wrt y-scale. Then using d3.line(), I added line in the svg. Then, the difficult part was adding tooltip to the plot as mouse hovers. So, I made one vertical line and circle elements and then use append('svg:rect') on that vertical line to trak mouse movements on canvas. Then, I defined mouseout, mouseover functions accordingly and in mousemove, I used d3.pointer(event) to get the exact position of mouse on the canvas. Then I used xLine.invert() to get values in the range of our original dataset. Since, I wanted the line only to appear on the x-axis ticks, I made use of Math.round() to get the x-axis ticks labels. Another tricky part was since I used d3.curveBasis(), the position of y for x-value is not exactly as provided on the dataset. So, I needed to find out the y-value for the given x on the plotted curve to position the circle. So, I made use of line.getPointAtLength() function to find out the position for circle element. Then finally, return the respective tooltip values.

**Bar chart:**<br>
Here, I have three datasets, so I made use of update function that takes different datasets and update the curve accordingly. Similar to line chart, firstly axes are added to svg element. Then I plotted two bar-charts. The blue one and the grey one. The grey bars are only displayed on hovering. I made use of x.bandwidth() to get width of bars to make sure that the grey bars look like the enlarged version of the blue one. The hovering features of the blue bars and grey bars are put same. Other different features like remove() and stroke-width:0 are used to remove the y-axis tick-labels and axis lines.

**Performance:**<br>
I made use of bootstrap to make sure the width changes dynamically so that it works fine on mobile devices, too. Also, since we have already preprocessed data using google colab, we are using updated dataframes which doesn't take much time to load.

**Overdelivery:**<br>
* To analyze and reach to a conclusion from the visualization plots, it is better to have more information. So, this plots doesn't seem to be more scalable/flexible. It is better to have a time slider on the bottom (which supports zooming and panning), so that user can select the time-frame they want to interact by themselves. Adding, zooming and panning is better because for plots with small width and height, when we have large datasets, then there is chance of misleading conclusions. For instance: what we think is not a big increase maybe a big increase in the actual value. Also, adding a button element to choose specific year in barplot is better for large datasets.<br>
* Also, for weekly-chart, I felt the x-axis tick labels can be more better. Like, it shows the starting day of the day only and it is difficult to know what that bar is showing until we hover to get the information. So, I would prefer to put (19-26) than just 19.
