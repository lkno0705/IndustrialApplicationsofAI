This codebook.txt file was generated on 20190917 by Wanda Marsolek and updated on 20220909 by Nicolai Haeni
-------------------
GENERAL INFORMATION
-------------------
1. Title of Dataset
MinneApple: A Benchmark Dataset for Apple Detection and Segmentation

2. Author Information

  Principal Investigator Contact Information
        Name: Nicolai Haeni
           Institution: University of Minnesota
           Address: Shepherd Laboratories, 100 Union St SE, Minneapolis, MN 55455
           Email: haeni001@umn.edu
	   ORCID: https://orcid.org/0000-0003-4042-3318

  Associate or Co-investigator Contact Information
        Name: Pravakar Roy
           Institution: University of Minnesota
           Address:
           Email:
	   ORCID:https://orcid.org/0000-0002-5410-1486

  Associate or Co-investigator Contact Information
           Name: Volkan Isler
           Institution: University of Minnesota
           Address: Shepherd Laboratories, 100 Union St SE, Minneapolis, MN 55455
           Email: isler@umn.edu
           ORCID: https://orcid.org/0000-0002-0868-5441

3. Date of data collection 201506 - 201609 

4. Geographic location of data collection:  University of Minnesota Horticultural Research Center

5. Information about funding sources that supported the collection of the data:
Sponsorship: USDA NIFA MIN-98-G02

--------------------------
SHARING/ACCESS INFORMATION
-------------------------- 
1. Licenses/restrictions placed on the data:
Attribution-NonCommercial-ShareAlike 3.0 United States

2. Links to publications that cite or use the data:
Häni, N, Roy, P, Isler, V. A comparative study of fruit detection and counting methods for yield mapping in apple orchards. Journal of Field Robotics. 2019; 1– 20. https://doi.org/10.1002/rob.21902

3. Links to other publicly accessible locations of the data:
Project website: http://rsn.cs.umn.edu/index.php/MinneApple
GitHub Repository: https://github.com/nicolaihaeni/MinneApple

4. Recommended citation for the data:
Haeni, Nicolai; Roy, Pravakar; Isler, Volkan. (2019). MinneApple: A Benchmark Dataset for Apple Detection and Segmentation. Retrieved from the Data Repository for the University of Minnesota, http://hdl.handle.net/11299/206575.

---------------------
DATA & FILE OVERVIEW
---------------------
1. File List
   A. Filename: counting.tar.gz        
      Short description:    Images of modeling/testing (2,875 JPG files), training (64,595 PNG files), and validation (3,395 PNG files)   

   B. Filename: detection.tar.gz       
      Short description:  Images and ground truth including test images (331 PNG files), train images (670 PNG files), and mask images (670 PNG files)      
   
   C. Filename: test_data.zip    
        Short description:  Contains our release of the test labels for counting (2,875 labels), detection (.json file with COCO file annotations) and segmentation (331 masked segmentation images). This file was released and added to the DRUM record on 2022-09-12.

2. Relationship between files:        
The counting and detection data are used to solve two different subproblems of the larger problem that is yield estimation.
Yield estimation relies on accurate detection of the fruit. Since fruit can be clustered together, it is necessary to use a separate algorithm for counting (in most cases).
Data is provided to develop and test algorithms for both subproblems.

--------------------------
METHODOLOGICAL INFORMATION
--------------------------
Description of methods used for collection/generation of data: 
video footage from different sections of the orchard using a standard Samsung Galaxy S4 cell phone. During data collection, video footage was acquired by facing the camera horizontally at a single side of a tree row. Individual images were extracted from these video sequences. 

-----------------------------------------
DATA-SPECIFIC INFORMATION FOR: Counting
-----------------------------------------
Includes 3 main folders: Test, Train, Val
The train folder contains images and ground truth labels for model training. The val folder contains validation examples to test ones model. The test folder contains test examples without ground truth. We release the ground truth labels in test_data.zip. Alternatively, you can upload your data to a public competition and we compare them against the ground truth for you. See the project page for more details.

-----------------------------------------
DATA-SPECIFIC INFORMATION FOR: Detection
-----------------------------------------
Includes 2 main folders: Test images and Train images
Test images: include Datasets labled 1-4 internal designations. They mark different orchard rows from which the data was acquired. Front and back similarly means that data was taken either from the front of a tree row or from the back. We release the ground truth labels in test_data.zip. Alternatively, you can upload your data to a public competition and we compare them against the ground truth for you. See the project page for more details. 
Train images: include image folder and mask folder-- The images in the image folder contain the color image and the masks folder contains a corresponding mask with labels for the fruits. These masks can be used as ground truth to train models for apple detection.







