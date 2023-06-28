# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 00:15:56 2023

@author: navee
"""

import streamlit as st
from PIL import Image


st.set_page_config(layout="wide")


def main():
    
   
    # Sidebar
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ['Home','About Me'])

    # Home page
    if page == 'Home':
        st.title('"Journey to Creating a Population Density Map Using Rayshader in R and QGIS & Aerialod"')

        image = Image.open("1.jpg")

        st.image(image, use_column_width=True)

        # Subtitle or header
        st.header("Motivation and Introduction")
        
    
        # Content
        st.write("""
        In today's digital era, inspiration can strike from the most unexpected corners. For me, it was an intriguing density plot of France, casually spotted on a LinkedIn post, that ignited my curiosity. The captivating design, complexity, and depth of the plot left me in awe. Upon researching, I discovered it was crafted using Rayshader and R - tools I had no previous experience with. However, I was not deterred; instead, I saw this as an opportunity to learn and explore, so I decided to recreate a similar plot for the UK.
        
        I owe a great deal to the online coding community for the assistance I received throughout my learning process. I found a guiding light in the form of Spencer Schien, Pecners ([GitHub Profile](https://github.com/Pecners)), and notably, the AI developed by OpenAI, ChatGPT. My encounter with ChatGPT was a revelation - it showcased the power of artificial intelligence and its capacity to provide solutions and transform data effectively.
        
        Learning R and dealing with a new programming language was not without its challenges. There were times when the enormity of the data and the computational demands of plotting tested my patience. I was on the verge of giving up, but thanks to ChatGPT, I overcame those hurdles and kept progressing.
        
        Simultaneously, I realized that QGIS and Aerialod could make the process more efficient and less computationally heavy. Thus, my initial objective evolved from merely creating a population density plot to a broader goal of understanding and harnessing the potential of these technologies.
        
        This web application documents my journey of exploration and learning, the challenges I faced, and how I overcame them. It shares the code and processes I used, hoping to inspire and assist others who wish to venture into similar projects.
        
        Beyond the successful creation of the population density plot, this endeavor taught me that with a solid understanding of the basics, a splash of determination, and a good dose of curiosity, any programming language can be harnessed to bring our imagination to life.
        
    
        """)


        # Data Used Section
        st.header("Data Used")
        
        # Content
        st.write("""
        Creating a detailed and accurate population density plot necessitates robust and comprehensive data. I acquired the data for this project from two reputable sources: Kontur and WorldPop Hub.
        
        **Rayshader with R:**  
        For the Rayshader plot, the dataset was obtained from Kontur, a platform that offers a wide array of geospatial data. The specific dataset I used is titled 'United Kingdom of Great Britain and Northern Ireland: Population Density'. It was updated on June 30, 2022 and is part of the 'Kontur - Population Density for 400m H3 Hexagons' data series. This dataset can be downloaded from [here](https://data.humdata.org/organization/kontur?groups=gbr&q=&sort=if(gt(last_modified%2Creview_date)%2Clast_modified%2Creview_date)%20desc&ext_page_size=25).
        
        The dataset is structured using the H3: Hexagonal Hierarchical Spatial Index, and the population is calculated based on overlapping Global Human Settlement Layer (GHSL) with Facebook High Resolution Settlement Layer (HRSL) population data. It also uses OpenStreetMap data to constrain known artifacts.
        
        The dataset's metadata includes the H3 index of each hexagon, total population inside each hexagon, and the geometry (Polygon, EPSG:3857) of each hexagon.
        
        It's important to note that this dataset was primarily designed to support visualization behind the disaster.ninja project and may not be suitable for all specific needs. Hence, it's recommended to contact the dataset provider if you need custom processing or a higher resolution version of this dataset.
        
        **QGIS and Aerialod:**  
        For the process involving QGIS and Aerialod, I used data from the WorldPop Hub, which provides detailed geospatial datasets. The specific dataset used for this process is 'the spatial distribution of population density of UK 2020'. It can be downloaded from [here](https://hub.worldpop.org/geodata/summary?id=44435).
        
        The dataset is designed to estimate population density per grid-cell and is available in both Geotiff and ASCII XYZ formats at a resolution of 30 arc (approximately 1km at the equator). The projection used is the Geographic Coordinate System, WGS84.
        
        This dataset uses a Random Forest-based dasymetric redistribution to map the number of people per square kilometer. It is important to mention that the dataset was produced on June 22, 2020.
        
        Both datasets are publicly available and licensed under the Creative Commons Attribution International license, ensuring that they can be freely used, shared, and built upon, provided attribution is given to the creators.
        
        Understanding the structure and composition of the datasets was crucial in the process of creating the population density plot. It provided insights into the data's nature, how it is organized, and how to manipulate it to achieve the desired visualization. For those interested in undertaking similar projects, I highly recommend familiarizing oneself with the data before beginning the coding and visualization processes.
        """)
        
        
        # Plot Creation Process Section
        st.header("Plot Creation Process")
        
        # Content
       # Plot Creation Process Section
        st.header("Plot Creation Process")
        
        # Content
        st.subheader("Rayshader")
        st.write("""
        Rayshader is an open-source R package for producing 2D and 3D data visualizations. Rayshader uses elevation of points in a dataset to create 3D visualizations of landscapes, and it can also overlay these landscapes with various attributes such as shadows or water bodies. It's a powerful tool that's often used in geospatial data analysis to visualize topographical details.
        
        Rayshader has found application in a variety of fields such as environmental science, where it can be used to visualize terrain and water bodies. It's also used in urban planning and construction, where 3D visualization of terrain can aid in the planning of infrastructure.
        """)
        
        st.subheader("Code Explanation")
        
        st.markdown("### Loading libraries and reading data")
        st.code("""
        # Load libraries
        library(sf)
        library(rnaturalearth)
        library(raster)
        library(ggplot2)
        library(stars)
        
        # Read data
        data <- st_read("D:/Rayshader R/output.gpkg")
        """, language="r")
        st.write("""
        The code begins by loading necessary libraries. The sf, raster, and stars packages are used for handling and processing spatial data, rnaturalearth is for getting geographical data, and ggplot2 is for data visualization. The st_read function from sf is then used to read the geopackage file containing your data.
        """)
        
        st.markdown("### Getting world map data and subset for the United Kingdom")
        st.code("""
        # Get world map data
        world_map <- ne_countries(scale = "medium", returnclass = "sf")
        
        # Filter for the United Kingdom
        uk_map <- subset(world_map, admin == "United Kingdom")
        
        # Plot UK map
        ggplot() + geom_sf(data = uk_map) + ggtitle("Map of the United Kingdom")
        """, language="r")
        st.write("""
        The ne_countries function from rnaturalearth package is used to fetch world map data. The world map data is then subsetted to get data for the UK only using the subset function. The ggplot function from ggplot2 is then used to plot the UK map.
        """)
        
        st.markdown("### Checking and transforming CRS")
        st.code("""
        # Check CRS of both datasets
        crs_data <- st_crs(data)
        crs_uk_map <- st_crs(uk_map)
        
        # Transform CRS if they are not the same
        if (crs_data != crs_uk_map) {
          data <- st_transform(data, crs_uk_map)
        }
        """, language="r")
        st.write("""
        The st_crs function from sf is used to check the Coordinate Reference System (CRS) of both the datasets. If the CRS of the two datasets doesn't match, the CRS of your data is transformed to match that of the UK map data using the st_transform function.
        """)
        
        st.markdown("### Intersecting data")
        st.code("""
        # Intersect data
        intersected_data <- st_intersection(data, uk_map)
        """, language="r")
        st.write("""
        The st_intersection function from sf is used to intersect your data with the UK map data. This operation effectively restricts your data to the UK only.
        """)
        
        st.markdown("### Calculating aspect ratio")
        st.code("""
        # Get bounding box
        bb <- st_bbox(intersected_data)
        
        # Calculate aspect ratio
        width <- st_distance(st_point(c(bb["xmin"], bb["ymin"])), st_point(c(bb["xmax"], bb["ymin"]"]))
        height <- st_distance(st_point(c(bb["xmin"], bb["ymin"])), st_point(c(bb["xmin"], bb["ymax"])))
        aspect_ratio <- width / height
        """, language="r")
        st.write("""
        The st_bbox function is used to get the bounding box of the intersected data. The st_distance function is then used to calculate the width and height of the bounding box, which are then used to calculate the aspect ratio.
        """)
        
        st.markdown("### Rasterizing data")
        st.code("""
        # Rasterize data
        uk_rast <- st_rasterize(intersected_data, nx = floor(3000 * aspect_ratio), ny = 3000)
        """, language="r")
        st.write("""
        The st_rasterize function is used to rasterize the intersected data. This operation converts the vector data into raster data, where each pixel represents a geographic area.
        """)
        
        st.markdown("### Converting raster to matrix")
        st.code("""
        # Convert to matrix
        mat <- matrix(uk_rast$population, nrow = 3000, ncol = floor(3000 * aspect_ratio))
        """, language="r")
        st.write("""
        The raster data is then converted into a matrix. Each cell in the matrix represents the population density at a specific geographical location.
        """)
        
        # Generating 3D plot
        st.subheader("Generating 3D plot")
        st.write("""
        This part of the code is where we convert our population density matrix into a 3D visual representation using the rayshader package. The overall objective here is to create a 3D relief map where the height and color intensity represent the population density.
        """)
        
        st.markdown("### Load the necessary libraries for 3D rendering and color palettes")
        st.code("""
        library(rayshader)
        library(MetBrewer)
        library(rgl)
        """, language="r")
        st.write("""
        The rayshader package in R is primarily used for producing 2D and 3D data visualizations. It is uniquely capable of creating stunning 3D models using only a dataset and the elevation matrix.
        
        MetBrewer is an R package used for creating color palettes, which can be applied to the 3D plot to aid in visualization.
        
        rgl is a package for creating interactive 3D plots. It provides a medium where rayshader can plot its 3D data visualizations.
        """)
        
        st.markdown("### Create a color palette")
        st.code("""
        c1 <- met.brewer("OKeeffe2")
        """, language="r")
        st.write("""
        Here, we create a color palette named c1 using the "OKeeffe2" palette from the met.brewer package. Color palettes help in making visualizations more aesthetically pleasing and easier to understand.
        """)
        
        st.markdown("### Generate a texture using the color palette")
        st.code("""
        texture <- grDevices::colorRampPalette(c1, bias = 2)(256)
        """, language="r")
        st.write("""
        We then generate a texture using the color palette created above. The colorRampPalette function is used to interpolate a set of colors (our color palette c1 in this case). The texture created here will be applied to the 3D plot to denote population density. The bias parameter controls the color interpolation process - a bias < 1 emphasizes lower density areas, while a bias > 1 highlights higher density areas.
        """)
        
        st.markdown("### Close any existing rgl windows")
        st.code("""
        rgl::close3d()
        """, language="r")
        st.write("""
        Before we start creating our 3D plot, we ensure to close any existing 3D plotting windows using the close3d function from rgl. This step is a good practice to avoid overplotting or confusion from previous plots.
        """)
        
        st.markdown("### Create the 3D plot")
        st.code("""
        mat %>% 
          height_shade(texture = texture) %>% 
          plot_3d(heightmap = mat, zscale = 100 / 5, solid = FALSE, shadowdepth = 0)
        """, language="r")
        st.write("""
        Finally, we create our 3D plot using the plot_3d function from rayshader. We pipe (%>%) our matrix mat to the height_shade function, which calculates the ambient shadows based on the sun's relative position. We provide the texture we created earlier to this function.
        
        In plot_3d, the heightmap argument takes our matrix mat, and zscale is used to exaggerate the relief of the 3D plot. The solid argument is set to FALSE to generate a 3D surface plot, and shadowdepth is set to zero, meaning no shadow will be cast by the 3D plot.
        """)
        
        # Setting the CameraAngle and Saving the 3D Plot
        st.subheader("Setting the Camera Angle and Saving the 3D Plot")
        
        st.markdown("### Set the camera angle and zoom for the 3D plot")
        st.code("""
        render_camera(theta = -20, phi = 45, zoom = .8)
        """, language="r")
        st.write("""
        render_camera is a function from the rayshader package which sets the camera angle for viewing the 3D plot. The parameters theta and phi define the viewing angles, where theta rotates the view around the z-axis, and phi rotates the view around the y-axis. The zoom parameter, as the name implies, sets the zoom level for the 3D plot.
        """)
        
        st.markdown("### Define the output file name")
        st.code("""
        outfile <- "final_plot.png"
        """, language="r")
        st.write("""
        We set the name of the output file where our final 3D plot will be saved.
        """)
        
        st.markdown("### Start rendering time")
        st.code("""
        start_time <- Sys.time()
        cat("Rendering started at:", start_time, "\\n")
        """, language="r")
        st.write("""
        We get the current time using Sys.time() and save it to start_time. We then print a message to indicate the rendering process has started.
        """)
        
        st.markdown("### Create the output file if it doesn't exist")
        st.code("""
        if (!file.exists(outfile)) {
          png::writePNG(matrix(1), target = outfile)
        }
        """, language="r")
        st.write("""
        Before rendering the plot, we check if the output file already exists using file.exists(). If it doesn't, we create an empty PNG file with the specified name using writePNG() from the png package.
        """)
        
        st.markdown("### Render the high-quality plot")
        st.code("""
        render_highquality(
          filename = outfile,
          interactive = FALSE,
          lightdirection = 280,
          lightaltitude = c(20, 80),
          lightcolor = c(c1[2], "white"),
          lightintensity = c(600, 100),
          samples = 450,
          width = 6000,
          height = 6000
        )
        """, language="r")
        st.write("""
        The render_highquality() function from the rayshader package is used to render the plot in high quality. We provide our outfile name to the filename parameter. The interactive argument set to FALSE means the plot will be non-interactive (i.e., static).
        
        The lightdirection, lightaltitude, lightcolor, and lightintensity parameters are used to set the lighting conditions for the 3D plot, to make it more realistic. samples parameter sets the number of random samples to generate per pixel for antialiasing. width and height parameters set the dimensions of the output image in pixels.
        """)
        
        st.markdown("### End rendering time")
        st.code("""
        end_time <- Sys.time()
        diff <- end_time - start_time
        cat("Rendering completed in:", diff, "\\n")
        """, language="r")
        st.write("""
        Finally, we mark the end of the rendering process by getting the current time and calculating the difference from the start time. This gives us the total time taken for the rendering process. The difference in time is printed out for us to know how long the rendering process took.
        """)


        # Introduction to QGIS and Aerialod
        st.header("2.QGIS and Aerialod")
        st.subheader("Introduction to QGIS and Aerialod")
        st.write("""
        QGIS is a free and open-source cross-platform desktop geographic information system (GIS) application that supports viewing, editing, and analysis of geospatial data. It provides a range of functionalities to manipulate and analyze spatial data.
        
        Aerialod is a software that allows rendering high-quality 3D plots in real time. It takes spatial data, such as an elevation map, as input and outputs a realistic 3D render.
        """)
        
        st.markdown("Links to download:")
        st.markdown("[QGIS](https://qgis.org/en/site/forusers/download.html)")
        st.markdown("[Aerialod](http://ephtracy.github.io/)")
        
        st.write("""
        Both of these tools have GUIs (Graphical User Interfaces), making it easier for non-technical users to interact with their functionalities.
        """)
        
        st.markdown("### Importing the Spatial Data to QGIS")
        st.write("""
        Begin by importing the TIFF spatial data file into QGIS. To do this, navigate to "Layer" in the top menu, select "Add Layer", and then "Add Raster Layer". Locate your TIFF file and click "Open".
        """)
        
        st.markdown("### Export the Layer")
        st.write("""
        Next, we need to export the raster layer to a new TIFF file that will be used in Aerialod. This is necessary to scale the image using pixel values in the range of 0 to 255, where 0 is black and 255 is white. This conversion is necessary because Aerialod interprets these grayscale values to represent different altitudes in the Z axis.
        
        To export, right-click on the layer and select "Export". Then, click on "Save As". Choose the format as "Rendered Image" and select "TIFF" as the format. Finally, select a destination folder and click "OK".
        """)
        
        st.markdown("### Open the Rendered TIFF in Aerialod")
        st.write("""
        Open Aerialod and click on "Open". Select the TIFF file you just exported from QGIS. The result might not be satisfactory as there will be no land base. The lowest value in the original TIFF will be considered as the base height.
        """)
        
        st.markdown("### Adjusting the Layer Properties in QGIS")
        st.write("""
        Go back to QGIS and right-click on the layer again. Click on "Properties" and select the "Symbology" tab. Change the Render type to "Singleband pseudocolor".
        
        In the "Min" field, set some value (ensure it's not zero) and set "Max" to 255. In the color ramp, select a two-color scheme: black to white. The "Min" value should correspond to black and "Max" to white. Click on "Apply" and then "OK".
        """)
        
        st.markdown("### Re-export the Layer")
        st.write("""
        Following the same steps as before, export the layer again. This newly exported TIFF will have better scaled altitudes for Aerialod to interpret.
        """)
        
        st.markdown("### Final Render in Aerialod")
        st.write("""
        Finally, import this last TIFF file into Aerialod. You can play around with different settings such as lighting, height of the hills, and other aspects to improve the visualization.
        
        Remember that these steps involve some trial and error to get the best output. Don't hesitate to adjust the parameters and export multiple times to achieve a satisfying result.
        
        This whole process demonstrates how powerfulopen-source tools can be in processing and visualizing complex geospatial data, enabling users to create detailed and accurate 3D representations.
        """)


        # Maps and Plots
        st.header("Maps and Plots")
        
        st.write("""
        Here are the maps and plots generated using QGIS and Aerialod.
        """)
        
        
        
        image = Image.open("UK_raw.png")

        st.image(image,caption="Plot generated by Aerialod (UK)", use_column_width=True)
        
        image = Image.open("2.jpg")

        st.image(image,caption="Plot generated by Aerialod", use_column_width=True)
        
        image = Image.open("india_raw.png")

        st.image(image,caption="Plot generated by Aerialod (India)", use_column_width=True)
        
        # Conclusion
        st.header("Conclusion")
        
        st.write("""
        Throughout this project, we embarked on an exciting journey that started with zero knowledge about R and QGIS and ended with a comprehensive understanding of how to use these tools to analyze and visualize geospatial data. This project was a vivid demonstration of how technology, specifically AI, empowers us to learn and apply complex tasks quickly and efficiently.
        
        With AI as our guide, we were able to navigate the complex landscapes of the R programming language, the intricacies of the spatial packages, and the functionalities of QGIS, breaking down each process into understandable, manageable steps. This facilitated learning and simplified the application of this knowledge to our specific use case - creating a 3D plot of the UK's population density.
        
        The results obtained from the 3D plot offer unique insights into the spatial distribution of the UK population, and the rendered image provides a visually striking representation of this data. It's remarkable to see how elevation and valleys of the 3D plot correspond to areas of high and low population density, respectively.
        
        This project demonstrates that a lack of prior knowledge should not be a deterrent in the world of data analysis and visualization. With the right resources, the learning curve can be overcome, and complex tasks can be made feasible.
        
        The methodologies and skills we've acquired through this project are transferable and can be applied to different datasets and in different domains. For example, a similar approach could be employed to visualize other geospatial data such as temperature or rainfall distribution, forest coverage, or even to map and understand the spread of diseases like COVID-19. The possibilities are endless.
        
        In terms of future work, there are many potential extensions of this project. For instance, one could incorporate time-series data to create animated 3D plots showing how population density has changed over time. Alternatively, additional datasets could be integrated into the analysis, such as economic or infrastructure data, to provide more nuanced insights into the population distribution.
        
        In conclusion, this project highlights the power of AI, not just in terms of conducting complex data analysis, but also in aiding learning and understanding. The ability of AI to break down complex tasks into comprehensible parts is truly revolutionizing the way we learn, work, and progress in the field of data science.
        """)

      
        # Resources
        st.subheader("Resources")
        
        st.write("""
        For those who are interested in learning more or exploring further, here are some valuable resources that were instrumental in the completion of this project:
        
        1. **GitHub Repository (QGIS)**: This repository contains the code and resources used in the QGIS part of the project. [Link to the repository](https://github.com/nani2357/QGIS.git).
        
        2. **GitHub Repository (Rayshader Sample Code)**: This repository by Pecners contains sample code for creating plots using Rayshader. It's a great resource for anyone looking to get started with Rayshader. [Link to the repository](https://github.com/Pecners/kontur_rayshader_tutorial).
        
        3. **YouTube Tutorial (Rayshader)**: This YouTube tutorial provides guidance on how to use Rayshader for creating 3D plots. It's a comprehensive guide that covers the basics and advanced features of Rayshader. [Watch the tutorial](https://www.youtube.com/watch?v=zgFXVhmKNbU&t=190s).
        
        4. **YouTube Tutorial (QGIS 3D Raytracing with Aerialod)**: This tutorial on YouTube provides guidance on how to use QGIS for 3D ray tracing with Aerialod. It's an excellent resource for learning how to create stunning 3D visualizations using QGIS and Aerialod. [Watch the tutorial](https://www.youtube.com/watch?v=tzsU7kSRNF8).
        """)






    elif page == "About Me":
        st.title('About Me')
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.write("""
            ## Naveen Kumar Kadampally
         
            ## Professional Background
    
           My career journey started as a **Civil Engineer** at RG Constructions where I honed my skills in construction management, contract management, and AutoCAD. My role here was multidimensional, and I was responsible for everything from supervising construction workers, ensuring site safety, to material quantity management. My stint at RG Constructions provided me with a strong foundation and a broad perspective of problem-solving, which was the cornerstone for my subsequent career transitions.
    
           
        """)
    
        with col2:
            image = Image.open("img.jpg")
            st.image(image, use_column_width=True)
    
        
        st.write("""
                 I then made a bold career switch into the technology domain as a **Software Test Analyst** at Unified Softech. Intrigued by the role of data in decision-making and the potential it had to revolutionize industries, I navigated my way into data analysis and data science.
    
                 My transformation into a **Data Analyst** was an exciting journey. After acquiring the IBM Data Science Professional Certification, I began leveraging my knowledge in various data analysis tools and Python libraries to derive valuable insights from complex datasets. I played a pivotal role in developing targeted marketing strategies and enhancing customer experience by managing customer complaints more efficiently.
    
                 Building on my data analysis experience, I am currently diving deeper into the realm of **Artificial Intelligence (AI) and Machine Learning**. I am exploring these technologies to build advanced models that can further streamline decision-making and efficiency in businesses.
    
                 ## Skills
    
                 My technical skills range from **AutoCAD** and **Revit** in the field of Civil Engineering to **Python**, **SQL**, **Tableau**, and **PowerBI** in Data Analysis. My knowledge of **Machine Learning algorithms** and **Data Visualization tools** has allowed me to create intuitive dashboards and powerful predictive models.
    
                 On the soft skills front, I pride myself on my strong **communication skills** and **project management** abilities. These skills have been instrumental in leading teams, managing projects, and effectively coordinating with stakeholders.
    
                 ## Projects
    
                 I have been involved in several exciting projects throughout my career journey. My key projects include a **Customer Segmentation Project** at Unified Softech where I used Machine Learning to segment customers based on their purchasing history. The outcome was a more personalized customer experience and improved customer retention rates.
    
                 I also embarked on a project focused on **Predictive Analysis of Sales Data**. This project involved creating a model that could accurately predict future sales based on historical data, helping the company to strategically plan their production and inventory management.
    
                 In a freelance capacity, I worked with a construction company to develop a **Machine Learning model for Green Concrete Strength Prediction**. The model made accurate predictions about the strength of the green concrete based on the composition of recycled materials. This innovative approach promoted sustainability in the construction industry.
    
                 Now, as I venture into AI and Deep Learning, I'm excited to work on more advanced projects that integrate these technologies. My current projects are aimed at exploring new frontiers in AI and I am thrilled about the potential outcomes.
                 """)
                 
                 
    
        st.write("""
        ## Certifications
    
    I have pursued several certifications to expand my knowledge base and validate my skills, including:
    
    - **IBM Data Science Professional Certification**: This certification provided a solid grounding in data science methodologies, and tools including Python, SQL, and data visualization.
    
    - **ISTQB Certified Tester**: This internationally recognized certification has honed my understanding of software testing techniques and principles. It played a pivotal role during my tenure as a Software Test Analyst at Unified Softech.
    
    - **Microsoft Power BI Certification**: This certification confirmed my expertise in using PowerBI for data analysis and visualization, enabling me to create effective and insightful dashboards.
    
    - **AutoCAD Certified User**: This certification validated my proficiency in AutoCAD software, which I utilized extensively during my tenure as a Civil Engineer.
    
        ## Learning Journey and Future Goals
    
        Transitioning from Civil Engineering to Software Testing, and then Data Science has been an incredible journey of learning and growth. This journey has taught me that technology's potential is boundless, and the more we learn, the more we can harness its power.
    
        As I venture further into the world of AI and Machine Learning, I aim to create more sophisticated models and solutions that can enhance decision-making and efficiency in businesses.
    
        I am also eager to contribute to the growing field of AI ethics, as I believe that responsible AI usage is crucial for future technological advancements. In line with this, I am working towards obtaining a certification in AI Ethics in the coming year.
    
        ## Personal Interests
    
        I have a profound affinity for the outdoors. I am captivated by nature and relish every opportunity to be outside, whether that's on sun-drenched beaches or in the verdant expanses of a forest. I find these moments to be incredibly refreshing and grounding, a perfect respite from the hustle and bustle of the tech world. 
    
        Mountains, in particular, hold a special allure for me. I love trekking through mountainous terrains and setting up camp under the stars. There's something incredibly serene about the stillness of the night, punctuated only by the gentle crackle of a campfire and the laughter and stories shared around it. 
    
        Lakes are another favorite escape of mine, especially those nestled in the heart of mountains. I enjoy boating and fishing, finding these activities to be both exciting and soothing. There's a unique sense of contentment I experience when I am casting a line out into the tranquil water, surrounded by the majesty of mountain peaks.
    
        Beyond my love for outdoor activities, I am an internet enthusiast. I spend a considerable amount of time surfing the web, staying updated on emerging trends and technologies. This curiosity extends to my professional life, as it helps me keep a pulse on the rapidly evolving tech landscape.
    
        My family plays a pivotal role in my life. I treasure the time spent watching movies with my children and exploring the outdoors with them. I believe these experiences foster their curiosity, teach them resilience, and create priceless memories.
    
        My interests, whether it's my love for nature or technology, or my devotion to family, shape who I am. They provide me with relaxation, continual learning, and cherished experiences – elements that I consider vital in life.
    
        ## Contact Information
    
        I'm always open to discussing data science, technology, and potential collaborations. You can reach me via email at [naveenkadampally@outlook.com](mailto:naveenkadampally@outlook.com).
    
        ### Social Media Profiles
        [![Instagram](https://img.shields.io/badge/-Instagram-black?style=flat-square&logo=instagram)](https://www.instagram.com/naveen.ka202/)
        [![LinkedIn](https://img.shields.io/badge/-LinkedIn-black?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/naveen-kumar-kadampally/)
        [![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=github)](https://github.com/nani2357)
    """)





if __name__ == "__main__":
    main()