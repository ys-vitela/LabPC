echo "decodificar y codificar archivos base64"
echo " "
echo "archivo codificado"
echo " "
echo | base64 cifra.txt > nuevo_cifra.txt
cat nuevo_cifra.txt
echo " "
echo "archivo descodificado"
echo " "
echo | base64 -d nuevo_cifra.txt > original_cifra.txt
cat original_cifra.txt
echo " "
echo "ahora en md5"
echo " "
echo | md5sum cifra.txt > md5_cifra.txt
cat md5_cifra.txt
echo " "
echo "vemos si funcinó"
echo " "
echo | md5sum -c md5_cifra.txt > md5_nuevo.txt
cat md5_nuevo.txt
