 <?php
   
   
   error_log("---------------------------------------------------------------- \n", 3, "/home/pi/tmp/AirlyN.txt");
   
   echo date('Y-m-d H:i:s');
   echo " - Odczyt danych Airly - Id = 509";echo "\r\n";echo "\r\n";
   
   error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/AirlyN.txt");
   error_log(" - Odczyt danych Airly\n", 3, "/home/pi/tmp/AirlyN.txt");
   
   echo date('Y-m-d H:i:s');
   echo " - Odpalamy WEB\n";
   $curl = curl_init();
  //Inicujemy curl
  curl_setopt($curl, CURLOPT_URL, 'https://airapi.airly.eu/v2/measurements/installation?installationId=509');
  // poprzedni Id=509
  //pobieramy dane
  curl_setopt($curl, CURLOPT_REFERER, "http://www.google.pl/");
  //ustawiamy refferer na www.google.pl (niektóre strony maj¹ zabezpieczenia
  $apiKey = '5d966716c6e84f61840e50f1345a2bed'; // should match with Server key
  $headers = array(
     'Accept: application/json',
	 'apikey: 5d966716c6e84f61840e50f1345a2bed'
  );
  //curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
  //pod¹¿amy za ewentualnym przekierowaniem
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
  //wyniku nie wyœwietlamy a zapisujemy do zmiennej co u³atwia prace nad nim
  curl_setopt($curl, CURLOPT_USERAGENT, 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)');
  //ustawiamy useragent (niektóre strony maj¹ zabezpieczenia)
  curl_setopt($curl, CURLOPT_TIMEOUT, 30);
  //Maxymalny czas po³¹czenia ze stron¹
  curl_setopt($curl, CURLOPT_HEADER, 1);
  //nie chcemy do³¹czaæ nag³ówka
  
  curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
  
  echo 'Curl error: ' . curl_error($curl);echo "\r\n";
  
  $response = curl_exec($curl);
  $info = curl_getinfo($curl);
  $http_code = curl_getinfo($curl, CURLINFO_HTTP_CODE);
  //uruchamiamy skonfigurowanego curla
  
  echo date('Y-m-d H:i:s');
  echo " - Dane pobrane z WEB"; echo "\r\n";
  echo $http_code;echo "\r\n";
  
  // Check HTTP status code
  if (!curl_errno($curl)) {
  switch ($http_code = curl_getinfo($curl, CURLINFO_HTTP_CODE)) {
    case 200:  # OK
      break;

    default:
      echo 'Unexpected HTTP code: ', $http_code, "\r\n";
  }
}
  
  
  echo substr($response,1,600);echo "\r\n";  
 
   
   $actualResponseHeaders = (isset($info["header_size"]))?substr($response,0,$info["header_size"]):"";
   $actualResponse = (isset($info["header_size"]))?substr($response,$info["header_size"]):"";

    //var_dump(json_decode( $actualResponse ));echo "\r\n";
 
   curl_close($curl);
  //zamykamy
   
   echo substr($actualResponse,1,100); echo "\r\n";
    
   //var_dump(json_decode($actualResponse));
   //var_dump(json_decode($actualResponse, True));
   
   
   
   $character = json_decode($actualResponse);
   
   if ($http_code == 200) {
     $message = "OK"; }
   else {
     $message = $character->{'message'};
     echo "Message         = "; echo $character->{'message'};echo "\r\n";	 }
   
   if ($message == "API rate limit exceeded") {
            $d[1] = 509;//mysqli_result($result,0,"Dana01");
			$d[2] = 0;//mysqli_result($result,0,"Dana02");
			$d[3] = 0;//mysqli_result($result,0,"Dana03");
			$d[4] = 0;//mysqli_result($result,0,"Dana04");
			$d[5] = 0;//mysqli_result($result,0,"Dana05");
			$d[6] = 0;//mysqli_result($result,0,"Dana06");
			$d[7] = 0;//mysqli_result($result,0,"Dana07");
			$d[8] = 0;//mysqli_result($result,0,"Dana08");
			$d[9] = 0;//mysqli_result($result,0,"Dana09");
			$d[10] = 99; }
   else {
     //echo $character;

     echo "--------------------------------------------------";echo "\r\n";
     //echo $var_dump->{'temperature'};echo "\r\n";
     //echo "--------------------------------------------------";echo "\r\n";
     //echo $var_dump;echo "\r\n";
     //echo "--------------------------------------------------";echo "\r\n";
      
     $d = array();
     $d[1] = 509;
     $d[2] = $character->{'current'}->indexes[0]->{'value'};
	 echo "fromDateTime = ".$d[2] ;echo "\r\n";
     $d[3] = $character->{'current'}->values[0]->{'value'};
	 echo "pm1             = ".$d[3] ;echo "\r\n";
     $d[4] = $character->{'current'}->values[1]->{'value'};
	 echo "pm25            = ".$d[4] ;echo "\r\n";
     $d[5] = $character->{'current'}->values[2]->{'value'};
	 echo "pm10            = ".$d[5] ;echo "\r\n";
     $d[6] = $character->{'current'}->values[3]->{'value'};
	 echo "pressure        = ".$d[6] ;echo "\r\n";
     $d[7] = $character->{'current'}->values[4]->{'value'};
	 echo "humidity        = ".$d[7] ;echo "\r\n";
     $d[8] = $character->{'current'}->values[5]->{'value'};
	 echo "temperature     = ".$d[8] ;echo "\r\n";
     $d[9] = 0;
	 echo "pollutionLevel  = ".$d[9] ;echo "\r\n";
     $d[10] = 0;
     //echo $d[1]; echo "\r\n";
     echo "--------------------------------------------------";echo "\r\n";
  }
  
  echo "\r\n";
  echo "Zapis do bazy mySQL "; echo "\r\n";
  
$con = mysqli_connect("mn14.webd.pl","van5656_Buderus","Baza911!");
if (!$con)
  {
    echo "Problem ";echo "\r\n";
//  die('Could not connect: ' . mysqli_error());
  }

mysqli_select_db($con, "van5656_Buderus");
//die('Could not connect: ' . mysqli_error());
$wynik = 0;

error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/AirlyN.txt");
error_log(" - SQL Start\n", 3, "/home/pi/tmp/AirlyN.txt");

error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/AirlyN.txt");
error_log(" - Dane kontrolne :  ", 3, "/home/pi/tmp/AirlyN.txt");
error_log($d[7], 3, "/home/pi/tmp/AirlyN.txt");
error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/AirlyN.txt");
error_log(" - Dane kontrolne :  ", 3, "/home/pi/tmp/AirlyN.txt");
error_log($d[8], 3, "/home/pi/tmp/AirlyN.txt");

if (($d[7] <> 0) && ($d[8] <> 0))
{
  echo "Próbujemy dodaæ" ;echo "\r\n";
  mysqli_query($con, "INSERT INTO AirlyPollution (Id, airQualityIndex, pm1, pm25, pm10, pressure, humidity, temperature, pollutionLevel, Error) 
  VALUES ($d[1], $d[2], $d[3], $d[4], $d[5], $d[6], $d[7], $d[8], $d[9], $d[10])")
  or //die('Insert Error: ' . mysqli_error());
  $wynik = 99;
}

if (($d[7] <> 0) && ($d[8] <> 0))
{
  echo "Próbujemy dodaæ - 1min : " ;
  $czas_akt = time() - 60;
  echo $czas_akt; echo "   "; 
  $created_date = date("Y-m-d H:i:s", $czas_akt);
  echo $created_date;echo "\r\n";
  $d[10] = 1;
  mysqli_query($con, "INSERT INTO AirlyPollution (DataCzas, Id, airQualityIndex, pm1, pm25, pm10, pressure, humidity, temperature, pollutionLevel, Error) 
  VALUES (FROM_UNIXTIME($czas_akt), $d[1], $d[2], $d[3], $d[4], $d[5], $d[6], $d[7], $d[8], $d[9], $d[10])")
  or //die('Insert Error: ' . mysqli_error());
  $wynik = 99;
}


error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/AirlyN.txt");
error_log(" - Probny zapis :  ", 3, "/home/pi/tmp/AirlyN.txt");
error_log($wynik, 3, "/home/pi/tmp/AirlyN.txt");
error_log("  ", 3, "/home/pi/tmp/AirlyN.txt");
error_log("- jezeli 0 - to zapis OK\n", 3, "/home/pi/tmp/AirlyN.txt");


if (($wynik == 99) || (($d[7] == 0) && ($d[8] == 0)))
{

echo "Odczyt starych danych z SQL"; echo "\r\n";

error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/AirlyN.txt");
error_log(" - Odczyt starych danych z SQL\n", 3, "/home/pi/tmp/AirlyN.txt");

$query="SELECT * FROM `AirlyPollution` where (airQualityIndex <> 0) and (Error = 0) order by DataCzas desc limit 1";
$result=mysqli_query($con, $query);
$num=mysqli_num_rows($result);
echo "Odczyt SQL = ".$num ; echo "\r\n";

$d[1] = 0;//mysqli_result($result,0,"Dana01");
$d[2] = 0;//mysqli_result($result,0,"Dana02");
$d[3] = 0;//mysqli_result($result,0,"Dana03");
$d[4] = 0;//mysqli_result($result,0,"Dana04");
$d[5] = 0;//mysqli_result($result,0,"Dana05");
$d[6] = 0;//mysqli_result($result,0,"Dana06");
$d[7] = 0;//mysqli_result($result,0,"Dana07");
$d[8] = 0;//mysqli_result($result,0,"Dana08");
$d[9] = 0;//mysqli_result($result,0,"Dana09");
$d[10] = 9;//mysqli_result($result,0,"Dana10");

if ($message == "API rate limit exceeded") {
  $d[1] = 509;
  $d[10] = 99; }
else {
  $d[1] = 509;
  $d[10] = 9; }

mysqli_query($con, "INSERT INTO AirlyPollution (Id, airQualityIndex, pm1, pm25, pm10, pressure, humidity, temperature, pollutionLevel, Error)
VALUES ($d[1], $d[2], $d[3], $d[4], $d[5], $d[6], $d[7], $d[8], $d[9],$d[10])") ;

	echo "Error - Empty record added"; echo "\r\n";
	error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/AirlyN.txt");
    error_log(" - Error - Empty record added (111)\n", 3, "/home/pi/tmp/AirlyN.txt");
}
else
{
  echo "OK - Correct record added"; echo "\r\n";
  error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/AirlyN.txt");
  error_log(" - OK - Correct record added\n", 3, "/home/pi/tmp/AirlyN.txt");
}


mysqli_close($con);

echo "Koniec SQL"; echo "\r\n";
error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/AirlyN.txt");
error_log(" - Koniec SQL\n", 3, "/home/pi/tmp/AirlyN.txt");










  $json_addr = 'http://dns4344.asuscomm.com:9281/json.htm?type=command&param=udevice';
  
  $json = 'http://dns4344.asuscomm.com:9281/json.htm?type=command&param=udevice&idx=2&nvalue=0&svalue=';
  $temp = trim($d[8]);
  $idx = '2';
  $jsonExe = $json_addr.'&idx='.$idx.'&nvalue=0&svalue='.$temp;
  echo $jsonExe;echo "\r\n";
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $jsonExe);
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($curl, CURLOPT_TIMEOUT, 30);
  curl_setopt($curl, CURLOPT_HEADER, 0);
  ob_start();
  $strona = curl_exec($curl);
  curl_close($curl);

  //echo "Strona "; echo $d[8];echo '\r\n>';
  //echo $strona;echo '\r\n>';
  //echo "Koniec strony";echo '\r\n>';

   
echo "Koniec zapisu do Domoticz"; echo "\r\n";

echo date('Y-m-d H:i:s');;echo "\r\n";
print "Koniec skryptu\n";

error_log(date('Y-m-d H:i:s'), 3, "/home/pi/tmp/AirlyN.txt");
error_log(" - Koniec scryptu \n\n", 3, "/home/pi/tmp/AirlyN.txt");

?> 
