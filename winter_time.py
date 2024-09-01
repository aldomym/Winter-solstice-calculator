from math import cos, pi
#Only valid for years between AD 1000 and AD 3000
year = 2024
Y = (year-2000)/1000
JDE_0 = 2451900.05952+365242.74049*Y-0.06223*Y**2-0.000823*Y**3+0.000832*Y**4
B_0 = 324.96
C_0 = 1934.136
b = pi/180*B_0
c = pi/180*C_0
T = (JDE_0-2451545)/36525
W = 35999.373*T-2.47
Delta_L = 1+0.0334*cos(W)+0.0007*cos(2*W)
S = 485*cos(b+c*T)
JDE = JDE_0+0.00001*S/Delta_L
Z = int(JDE + 0.5);
F = (JDE + 0.5) % 1
if Z < 2299161:
  A = Z
elif Z > 2299161:
  alpha = int((Z-1867216.25)/36524.25)
  A = Z + 1 + alpha - int(alpha/4);
B = A + 1524;
C = int((B-122.1)/365.25);
D = int(365.25*C);
E = int((B-D)/30.6001);
day = B - D - int(30.6001*E) + F
if E < 14:
  month = E - 1
elif E == 14 or E == 15:
  month = E - 13
if month > 2:
  year_0 = C - 4716
elif month == 1 or month == 2:
  year_0 = C - 4715;
time_0 = int(day)
Hour = day % 1;
hours = int(Hour*24);
mins = Hour*24 % 1
minutes = int(mins*60);
secs = mins*60;
print("Month:", month);
print("Day:", time_0)
print("Hours (TD):", hours);
print("Minutes:", minutes);
print("Seconds:", secs)
print("Note: TD means dynamical time")
