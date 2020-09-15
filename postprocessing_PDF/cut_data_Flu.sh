#!/bin/sh
rm -f *.data
base_value=100
for ((i=0;i<100;i++));
do
step=$[50+$i]
if [ $step -lt $base_value ];
then
    file='../Flu_000'$step'.vtk'
else
    file='../Flu_00'$step'.vtk'
fi
echo file=$file
cat $file | sed -n "72685, 75184"p | awk '{printf("%14.7e \n",$1)}' > Ma_Savage.data
cat $file | sed -n "70183, 72682"p | awk '{printf("%14.7e \n",$1)}' > Ma_dpm.data
cat $file | sed -n "50168, 52667"p | awk '{printf("%14.7e \n",$1)}' > Kn_frac.data
cat $file | sed -n "52670, 55169"p | awk '{printf("%14.7e \n",$1)}' > Kn_Mag_us.data
cat $file | sed -n "65179, 67678"p | awk '{printf("%14.7e \n",$1)}' > Kn_gran.data
cat $file | sed -n "47666, 50165"p | awk '{printf("%14.7e \n",$1)}' > Is.data
paste Ma_Savage.data Ma_dpm.data Kn_frac.data Kn_Mag_us.data Kn_gran.data Is.data | awk '{print $1"\t" $2 "\t" $3 "\t" $4 "\t" $5 "\t" $6}' >>all.data
done
