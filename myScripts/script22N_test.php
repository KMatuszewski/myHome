<?php
   
   
   error_log("---------------------------------------------------------------- \n", 3, "/home/pi/tmp/BuderusN.txt");
   
   echo "Odczyt danych Buderus FEC 101";echo '<br/>';echo '<br/>';
   echo date('Y-m-d H:i:s');echo '<br/>';
   
   error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/BuderusN.txt");
   error_log(" - Odczyt danych Buderus FEC 101\n", 3, "/home/pi/tmp/BuderusN.txt");
   
   echo "Odpalamy WEB\n"; echo '<br/>';
   $curl = curl_init();
  //Inicujemy curl

  curl_setopt($curl, CURLOPT_URL, 'http://192.168.5.251:801/http_in_030144.htm');
  //pobieramy dane
  curl_setopt($curl, CURLOPT_REFERER, "http://www.google.pl/");
  //ustawiamy refferer na www.google.pl (niekt�re strony maj� zabezpieczenia

  //curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
  //pod��amy za ewentualnym przekierowaniem
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
  //wyniku nie wy�wietlamy a zapisujemy do zmiennej co u�atwia prace nad nim
  curl_setopt($curl, CURLOPT_USERAGENT, 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)');
  //ustawiamy useragent (niekt�re strony maj� zabezpieczenia)
  curl_setopt($curl, CURLOPT_TIMEOUT, 30);
  //Maxymalny czas po��czenia ze stron�
  curl_setopt($curl, CURLOPT_HEADER, 0);
  //nie chcemy do��cza� nag��wka
  $strona144 = curl_exec($curl);
  //uruchamiamy skonfigurowanego curla
  curl_close($curl);
  //zamykamy
  
  echo date('Y-m-d H:i:s');;echo '<br/>';
  
  $curl = curl_init();
  //Inicujemy curl
  
  curl_setopt($curl, CURLOPT_URL, 'http://192.168.5.251:801/http_in_030160.htm');
  //pobieramy dane
  curl_setopt($curl, CURLOPT_REFERER, "http://www.google.pl/");
  //ustawiamy refferer na www.google.pl (niekt�re strony maj� zabezpieczenia

  //curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
  //pod��amy za ewentualnym przekierowaniem
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
  //wyniku nie wy�wietlamy a zapisujemy do zmiennej co u�atwia prace nad nim
  curl_setopt($curl, CURLOPT_USERAGENT, 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)');
  //ustawiamy useragent (niekt�re strony maj� zabezpieczenia)
  curl_setopt($curl, CURLOPT_TIMEOUT, 30);
  //Maxymalny czas po��czenia ze stron�
  curl_setopt($curl, CURLOPT_HEADER, 0);
  //nie chcemy do��cza� nag��wka
  $strona160 = curl_exec($curl);
  //uruchamiamy skonfigurowanego curla
  curl_close($curl);
  //zamykamy
  
  echo date('Y-m-d H:i:s');;echo '<br/>';
  
  echo $strona144; 
  echo $strona160; 

?> 