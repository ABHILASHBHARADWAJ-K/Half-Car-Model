
># Suspension Tuning of an Automobile: A Critical Analysis

Suspension of the vehicle defines the quality of ride comfort which is very essential for smooth handling characteristics. Other aspect of suspension is to improve the performance by minimising the stabilisation time which is achieved with the help of destructive resonance of front and rear vibrations. 

>## Mentors
Abhilash Bharadwaj K
>## Members
  Adithya Srihari Rao
  
  Dhiren V Bhandary
   
  Prathamesh Kiran Anvekar 

>## Aim

  

To design and optimise the suspension system of an automobile for an increased ride comfort and to achieve the better stabilisation time.

  

>## Introduction

Suspension system in the vehicles often decides the comfort of the driver and passengers and it is governed by simplified set four differential equations which accounts for the vertical motions of the sprung masses and unsprung masses of the vehicle along with body pitch. Pitch motion is taken into account with respect to the angle of tilt with respect to the centre of mass. 


  

>## Project Work

It consists of four major steps. 
1. Development of Quarter Car Model
2. Upgrading to Half Car Model
3. Data Extraction and Refining
4. Optimization and Implementation

  

>### Development of Quarter Car Model
A regular spring mass damping system is taken as the inspiration for setting up the physical equation of the Quarter-Car which literally means one - fourth of the vehicle. An improvement on the single degree of freedom system has led to the Quarter Car Model by adding an additional mass called as 'unsprung mass' which is a dual degree of freedom system. Models were built in Simulink for better user interactive experience. Model assumes a particular step input and the motion of the sprung and unsprung masses are as shown in the figure. 



![Quarter Car Model in Simulink](https://github.com/ABHILASHBHARADWAJ-K/Halfcarmodel/blob/main/QCM_SIMULINK.png)

![Comparision between sprung and unsprung masses in QCM](https://github.com/ABHILASHBHARADWAJ-K/Halfcarmodel/blob/main/comparision_QCM.png)

>### Upgrade to Half Car Model
  
Half Car Model is the extension of the Quarter Car Model where the front and rear ends of the unsprung masses are considered along with the pitch motion of the sprung mass which is a 4-Degree of Freedom system to extract the data with improved accuracy. 
Four degrees of freedom include the verical motions of two unsprung masses and combined sprung mass along with the picth motion of the body. 
For given spring stiffness values, damping coefficients were varied over a range of values which is decided by the preset damping ratio for a particular road profile. 

![Half Car Model](https://github.com/ABHILASHBHARADWAJ-K/Halfcarmodel/blob/main/HCM_Simulink.png)

![Road Profiles](https://github.com/ABHILASHBHARADWAJ-K/Halfcarmodel/blob/main/Roadprofiles_HCM.png)


>### Data Extraction & Refining

Data has been collected for parametrised road input and velocity with different damping factors which give various stabilisation times for different damping coefficients. Body is considered stable when the displacement amplitude reaches 2% of its max amplitude. Time-Amplitude data has been extracted in the excel sheet for various combinations of C1 and C2 for given road profile and for every (C1, C2) pair, there is an associated stabilization time (t) that is marked and listed out in a seperate sheet. The wheelbase defines the time of delay between the front and rear bump actions. Parameters taken in this model are of BMW M3, which can be altered according to the simulation.




  

>### Optimization & Implementation

The choice of degree of polynomial for regression is made in such a way as neither to underfit nor overfit the surface and is applied over the refined data which has the values of (C1, C2, t) triads to plot a 3-dimensional surface and the least stabilisation time is found over the surface with particular set of values of damping coefficients in the front and rear ends of the vehicle with the point of projection on the plane of damping coefficients. Further, in actual implementation dampers are fed with specific pressures inside the chambers to give that damping factor which makes the vehicle to stabilise faster. 

![3-D Polynomial Regression Model](https://github.com/ABHILASHBHARADWAJ-K/Halfcarmodel/blob/main/Result_HCM.png)


>### Further Work
Half car model can be extended to Full car model with a 7DoF system to perform the analysis for better accuracy of results. 


>## Conclusion
At any point, the road profile, velocity, spring stiffnesses can be altered in the process for the ease of analysis for various types of systems.

  

Skills acquired:

  
1. Establishing mathematical equations and solutions for physical problems from preliminary laws
2. Solving ordinary differential equations in Simulink
3. MATLAB coherence with Simulink
4. Exposure to data acquisition
5. Markdown and LaTeX languages for professional documentation of various mathematical equations and matrices  

>## References

[Half Car Model: A 4 DoF system](https://in.mathworks.com/matlabcentral/fileexchange/106045-half-car-model?s_tid=prof_contriblnk)


[Developing QCM in Simulink](https://youtu.be/xiR_WORuILQ)

Fundamentals of vehicle dynamics by Thomas D. Gillespie
