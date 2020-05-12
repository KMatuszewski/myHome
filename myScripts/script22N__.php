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
  //ustawiamy refferer na www.google.pl (niektóre strony maj¹ zabezpieczenia

  //curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
  //pod¹¿amy za ewentualnym przekierowaniem
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
  //wyniku nie wyœwietlamy a zapisujemy do zmiennej co u³atwia prace nad nim
  curl_setopt($curl, CURLOPT_USERAGENT, 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)');
  //ustawiamy useragent (niektóre strony maj¹ zabezpieczenia)
  curl_setopt($curl, CURLOPT_TIMEOUT, 30);
  //Maxymalny czas po³¹czenia ze stron¹
  curl_setopt($curl, CURLOPT_HEADER, 0);
  //nie chcemy do³¹czaæ nag³ówka
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
  //ustawiamy refferer na www.google.pl (niektóre strony maj¹ zabezpieczenia

  //curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
  //pod¹¿amy za ewentualnym przekierowaniem
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
  //wyniku nie wyœwietlamy a zapisujemy do zmiennej co u³atwia prace nad nim
  curl_setopt($curl, CURLOPT_USERAGENT, 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)');
  //ustawiamy useragent (niektóre strony maj¹ zabezpieczenia)
  curl_setopt($curl, CURLOPT_TIMEOUT, 30);
  //Maxymalny czas po³¹czenia ze stron¹
  curl_setopt($curl, CURLOPT_HEADER, 0);
  //nie chcemy do³¹czaæ nag³ówka
  $strona160 = curl_exec($curl);
  //uruchamiamy skonfigurowanego curla
  curl_close($curl);
  //zamykamy
  
  echo date('Y-m-d H:i:s');;echo '<br/>';
  
  //echo $strona144; 
  //echo $strona160; 
    
 $d = array();

for($k = 144; $k < 160; $k++)
{
  if ($k < 10) $tekst = $k.' = '; else $tekst = $k.' = ';
  //echo "A = ".$tekst; //echo '<br/>';
 
  $i = strpos($strona144,$tekst);
  //echo $i; echo '<br/>';
  
  //$l = $k + 1;
  //if ($l < 10) $tekst = $l.' = '; else $tekst = $l.' = ';
  //echo "B = ".$tekst; 
  //$j = strpos($strona114,$tekst);
  //echo $j; echo '<br/>';
  
  //echo substr($strona144, $i+6,10);
  //echo '!<br/>';
	
  if ($i !== false) 
    $d[$k-143] = substr($strona144, $i+6,8);
  else
    $d[$k-143] = 0;
	
  //if (is_numeric($d[$k])) $d[$k] = $d[$k];
  //else $d[$k] = 0;
  echo "R ".$k." = ".$d[$k-143];echo '<br/>';
}
  
 echo '<br/>';
 
for($k = 160; $k < 176; $k++)
{
  if ($k < 10) $tekst = $k.' = '; else $tekst = $k.' = ';
  //echo "A = ".$tekst; //echo '<br/>';
 
  $i = strpos($strona160,$tekst);
  //echo $i; echo '<br/>';
  
  //$l = $k + 1;
  //if ($l < 10) $tekst = $l.' = '; else $tekst = $l.' = ';
  //echo "B = ".$tekst; 
  //$j = strpos($strona114,$tekst);
  //echo $j; echo '<br/>';
  
  //echo substr($strona144, $i+6,10);
  //echo '!<br/>';
	
  if ($i !== false) 
    $d[$k-143] = substr($strona160, $i+6,8);
  else
    $d[$k-143] = 0;
	
  //if (is_numeric($d[$k])) $d[$k] = $d[$k];
  //else $d[$k] = 0;
  echo "R ".$k." = ".$d[$k-143];echo '<br/>';
}
  
 echo '<br/>';

 
  if ($d[1] > 200) $d[1] = $d[1] - 256;
  //if ($d[25] > 200) $d[25] = $d[25] - 256;
  if ($d[27] > 200) $d[27] = $d[27] - 256;
  
  $d[5] = $d[5] / 2;
  $d[12] = $d[12]*256*256 + $d[13]*256 + $d[14];
  $d[13] = $d[15];
  $d[14] = $d[16];
  $d[15] = $d[17];
  $d[16] = $d[18];
  $d[17] = $d[19];
  $d[18] = $d[20];
  $d[19] = $d[21];
  $d[20] = $d[22];
  $d[21] = $d[23];
  $d[22] = $d[24];
  $d[23] = $d[25];
  $d[24] = $d[26];
  $d[25] = $d[27];
  $d[26] = $d[28];
  $d[27] = $d[29];
  $d[28] = $d[30];
  $d[29] = $d[31];
		  
  
  //echo $d[16]; echo '<br/>';
  //echo $d[31];

  error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/BuderusN.txt");
  error_log(" - Temperatura pieca :  ", 3, "/home/pi/tmp/BuderusN.txt");
  error_log($d[17], 3, "/home/pi/tmp/BuderusN.txt");

  
  
  echo '<br/>';
  echo "Zapis do bazy mySQL "; echo '<br/>';
  
$con = mysqli_connect("mn14.webd.pl","van5656_Buderus","Baza911!");
if (!$con)
  {
    echo "Problem ";echo '<br/>';
//  die('Could not connect: ' . mysqli_error());
  }

mysqli_select_db($con, "van5656_Buderus");
//die('Could not connect: ' . mysqli_error());
$wynik = 0;

error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/BuderusN.txt");
error_log(" - SQL Start\n", 3, "/home/pi/tmp/BuderusN.txt");

error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/BuderusN.txt");
error_log(" - Dane kontrolne :  ", 3, "/home/pi/tmp/BuderusN.txt");
error_log($d[7], 3, "/home/pi/tmp/BuderusN.txt");
error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/BuderusN.txt");
error_log(" - Dane kontrolne :  ", 3, "/home/pi/tmp/BuderusN.txt");
error_log($d[8], 3, "/home/pi/tmp/BuderusN.txt");
for($k = 1; $k < 32; $k++)
{
  error_log($d[$k], 3, "/home/pi/tmp/BuderusN.txt");
}


if (($d[7] <> 0) && ($d[8] <> 0))
{
  echo "Próbujemy dodaæ" ;echo '<br/>';
  mysqli_query($con, "INSERT INTO Buderus (Dana01, Dana02, Dana03, Dana04, Dana05, Dana06, Dana07, Dana08, Dana09, Dana10, 
				     Dana11, Dana12, Dana13, Dana14, Dana15, Dana16, Dana17, Dana18, Dana19, Dana20,
				     Dana21, Dana22, Dana23, Dana24, Dana25, Dana26, Dana27, Dana28, Dana29, Dana30, 
				     Dana31, Status) 
  VALUES ($d[1], $d[2], $d[3], $d[4], $d[5], $d[6], $d[7], $d[8], $d[9], $d[10], 
        $d[11], $d[12], $d[13], $d[14], $d[15], $d[16], $d[17], $d[18], $d[19], $d[20],
	$d[21], $d[22], $d[23], $d[24], $d[25], $d[26], $d[27], $d[28], $d[29], $d[30],
	$d[31], 999)")
  or //die('Insert Error: ' . mysqli_error());
  $wynik = 99;
}

error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/BuderusN.txt");
error_log(" - Probny zapis :  ", 3, "/home/pi/tmp/BuderusN.txt");
error_log($wynik, 3, "/home/pi/tmp/BuderusN.txt");
error_log("  ", 3, "/home/pi/tmp/BuderusN.txt");
error_log("- jezeli 0 - to zapis OK\n", 3, "/home/pi/tmp/BuderusN.txt");


if (($wynik == 99) || (($d[7] == 0) && ($d[8] == 0)))
{

echo "Odczyt starych danych z SQL"; echo '<br/>';

error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/BuderusN.txt");
error_log(" - Odczyt starych danych z SQL\n", 3, "/home/pi/tmp/BuderusN.txt");

$query="SELECT * FROM `Buderus` where (Dana07 <> 0) and (Dana08 <> 0) and (Dana18 <> 0) and (Status = 999) order by data desc limit 1";
$result=mysqli_query($con, $query);
$num=1;//mysqli_num_rows($result);
echo "Odczyt SQL = ".$num ; echo '<br/>';

$d[1] = 0;//mysqli_result($result,0,"Dana01");
$d[2] = 0;//mysqli_result($result,0,"Dana02");
$d[3] = 0;//mysqli_result($result,0,"Dana03");
$d[4] = 0;//mysqli_result($result,0,"Dana04");
$d[5] = 0;//mysqli_result($result,0,"Dana05");
$d[6] = 0;//mysqli_result($result,0,"Dana06");
$d[7] = 0;//mysqli_result($result,0,"Dana07");
$d[8] = 0;//mysqli_result($result,0,"Dana08");
$d[9] = 0;//mysqli_result($result,0,"Dana09");
$d[10] = 0;//mysqli_result($result,0,"Dana10");
$d[11] = 0;//mysqli_result($result,0,"Dana11");
$d[12] = 0;//mysqli_result($result,0,"Dana12");
$d[13] = 0;//mysqli_result($result,0,"Dana13");
$d[14] = 0;//mysqli_result($result,0,"Dana14");
$d[15] = 0;//mysqli_result($result,0,"Dana15");
$d[16] = 0;//mysqli_result($result,0,"Dana16");
$d[17] = 0;//mysqli_result($result,0,"Dana17");
$d[18] = 0;//mysqli_result($result,0,"Dana18");
$d[19] = 0;//mysqli_result($result,0,"Dana19");
$d[20] = 0;//mysqli_result($result,0,"Dana20");
$d[21] = 0;//mysqli_result($result,0,"Dana21");
$d[22] = 0;//mysqli_result($result,0,"Dana22");
$d[23] = 0;//mysqli_result($result,0,"Dana23");
$d[24] = 0;//mysqli_result($result,0,"Dana24");
$d[25] = 0;//mysqli_result($result,0,"Dana25");
$d[26] = 0;//mysqli_result($result,0,"Dana26");
$d[27] = 0;//mysqli_result($result,0,"Dana27");
$d[28] = 0;//mysqli_result($result,0,"Dana28");
$d[29] = 0;//mysqli_result($result,0,"Dana29");
$d[30] = 0;//mysqli_result($result,0,"Dana30");
$d[31] = 0;//mysqli_result($result,0,"Dana31");

mysqli_query($con, "INSERT INTO Buderus (Dana01, Dana02, Dana03, Dana04, Dana05, Dana06, Dana07, Dana08, Dana09, Dana10, 
				     Dana11, Dana12, Dana13, Dana14, Dana15, Dana16, Dana17, Dana18, Dana19, Dana20,
				     Dana21, Dana22, Dana23, Dana24, Dana25, Dana26, Dana27, Dana28, Dana29, Dana30, 
				     Dana31, Status)
VALUES ($d[1], $d[2], $d[3], $d[4], $d[5], $d[6], $d[7], $d[8], $d[9], $d[10], 
        $d[11], $d[12], $d[13], $d[14], $d[15], $d[16], $d[17], $d[18], $d[19], $d[20],
	$d[21], $d[22], $d[23], $d[24], $d[25], $d[26], $d[27], $d[28], $d[29], $d[30],
	$d[31], 111)") ;

	echo "Error - Empty record added"; echo '<br/>';
	error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/BuderusN.txt");
    error_log(" - Error - Empty record added (111)\n", 3, "/home/pi/tmp/BuderusN.txt");
}
else
{
  echo "OK - Correct record added"; echo '<br/>';
  error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/BuderusN.txt");
  error_log(" - OK - Correct record added\n", 3, "/home/pi/tmp/BuderusN.txt");
}


mysqli_close($con);

echo "Koniec SQL"; echo '<br/>';
error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/BuderusN.txt");
error_log(" - Koniec SQL\n", 3, "/home/pi/tmp/BuderusN.txt");

echo "Zapis do Domoticz"; echo '<br/>';
error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/BuderusN.txt");
error_log(" - Zapis danych do Domoticz\n", 3, "/home/pi/tmp/BuderusN.txt");

  $json_addr = 'http://dns4344.asuscomm.com:9281/json.htm?type=command&param=udevice';
  
  
  $json = 'http://dns4344.asuscomm.com:9281/json.htm?type=command&param=udevice&idx=3&nvalue=0&svalue=';
  $temp = trim($d[18]);
  $idx = '6';
  $jsonExe = $json_addr.'&idx='.$idx.'&nvalue=0&svalue='.$temp;
  echo $jsonExe;echo '<br/>';
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $jsonExe);
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($curl, CURLOPT_TIMEOUT, 30);
  curl_setopt($curl, CURLOPT_HEADER, 0);
  ob_start();
  $strona = curl_exec($curl);
  curl_close($curl);

  echo "Strona "; echo $d[18];echo '<br>';
  echo $strona;echo '<br>';
  echo "Koniec strony";echo '<br>';
  
  $json = 'http://dns4344.asuscomm.com:9281/json.htm?type=command&param=udevice&idx=4&nvalue=0&svalue=';
  $temp = trim($d[1]);
  $jsonExe = $json.$temp;
  echo $jsonExe;echo '<br/>';
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $jsonExe);
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($curl, CURLOPT_TIMEOUT, 30);
  curl_setopt($curl, CURLOPT_HEADER, 0);
  ob_start();
  $strona = curl_exec($curl);
  curl_close($curl);

  $json = 'http://dns4344.asuscomm.com:9281/json.htm?type=command&param=udevice&idx=5&nvalue=0&svalue=';
  $temp = trim($d[25]);
  $jsonExe = $json.$temp;
  echo $jsonExe;echo '<br/>';
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $jsonExe);
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($curl, CURLOPT_TIMEOUT, 30);
  curl_setopt($curl, CURLOPT_HEADER, 0);
  ob_start();
  $strona = curl_exec($curl);
  curl_close($curl);
  echo "Strona "; echo $d[18];echo '<br>';  echo $strona;echo '<br>';  echo "Koniec strony";echo '<br>';
  
  // Temperatura za³¹czenia palnika
  $temp = trim($d[13]);  $idx = '7';
  $jsonExe = $json_addr.'&idx='.$idx.'&nvalue=0&svalue='.$temp;
  echo $jsonExe;echo '<br/>';
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $jsonExe);
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($curl, CURLOPT_TIMEOUT, 30);
  curl_setopt($curl, CURLOPT_HEADER, 0);
  ob_start();
  $strona = curl_exec($curl);
  curl_close($curl);
  echo "Strona "; echo $d[15];echo '<br>';  echo $strona;echo '<br>';  echo "Koniec strony";echo '<br>';
  
  // Temperatura wy³¹czenia palnika
  $temp = trim($d[14]);  $idx = '8';
  $jsonExe = $json_addr.'&idx='.$idx.'&nvalue=0&svalue='.$temp;
  echo $jsonExe;echo '<br/>';
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $jsonExe);
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($curl, CURLOPT_TIMEOUT, 30);
  curl_setopt($curl, CURLOPT_HEADER, 0);
  ob_start();
  $strona = curl_exec($curl);
  curl_close($curl);
  echo "Strona "; echo $d[16];echo '<br>';  echo $strona;echo '<br>';  echo "Koniec strony";echo '<br>';
  
  
  //Palnik
  if ($d[17] == 1)
  {
	$jsonExe = 'http://dns4344.asuscomm.com:9281/json.htm?type=command&param=switchlight&idx=10&switchcmd=On';
  }
  else
  {
	$jsonExe = 'http://dns4344.asuscomm.com:9281/json.htm?type=command&param=switchlight&idx=10&switchcmd=Off';
  }
  echo $jsonExe;echo '<br/>';
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $jsonExe);
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($curl, CURLOPT_TIMEOUT, 30);
  curl_setopt($curl, CURLOPT_HEADER, 0);
  ob_start();
  $strona = curl_exec($curl);
  curl_close($curl);
  echo "Palnik - "; echo $d[17];echo '<br>';  echo $strona;echo '<br>';  echo "Koniec strony";echo '<br>';
  
  
echo "Koniec zapisu do Domoticz"; echo '<br/>';

echo date('Y-m-d H:i:s');;echo '<br/>';
print "Koniec skryptu\n";

error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/BuderusN.txt");
error_log(" - Koniec scryptu \n\n", 3, "/home/pi/tmp/BuderusN.txt");

?> 
