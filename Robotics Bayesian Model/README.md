# Robotics Bayesian Model

Making predictions on Robot Execution Failures.

A robotic arm performs manipulation maneuvers and sometimes it has some flaw
that has to do with a collision, a piece movement failure, etc. The robot must know what kind of fault
has taken place in order to make a decision and go on with the task at hand.

#### Data

**Original Owner and Donor**

* Luis Seabra Lopes and Luis M. Camarinha-Matos
* Universidade Nova de Lisboa,
* Monte da Caparica, Portugal

Date Donated: ​April 23, 1999


#### Features:

All features are numeric although they are integer valued only. Each feature represents a force or a
torque measured after failure detection; each failure instance is characterized in terms of 15
force/torque samples collected at regular time intervals starting immediately after failure detection;
The total observation window for each failure instance was of 315 ms.

Each example is described as follows:

     class
      Fx1   Fy1   Fz1   Tx1   Ty1   Tz1
      Fx2   Fy2   Fz2   Tx2   Ty2   Tz2
      ......
      Fx15  Fy15  Fz15  Tx15  Ty15  Tz15

where Fx1 ... Fx15 is the evolution of force Fx in the observation window, the same for Fy, Fz and the
torques; there is a total of 90 features.

The first column in Train-set is the class of each row.

* Normal (1)
* Bottom collision (2)
* Bottom obstruction (3)
* Collision in part (4)
* Collision in tool (5)


#### Dependencies

```
$ pip install -r requirements.txt
```