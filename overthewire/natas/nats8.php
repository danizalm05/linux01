#!/usr/bin/php

<?php

#Running php <file name>
echo   "\n\n";
$e1 = '3d3d516343746d4d6d6c315669563362';
echo 'e1 encodedSecret = ',$e1, "\n\n";

$e2 = hex2bin($e1);
echo"e2 hex2bin = ",$e2, "\n\n" ;

$e3 = strrev($e2 );
echo "e3 strrev = ",$e3, "\n\n" ;

$e4 = base64_decode($e3);
echo "e4 base64_decode = ",$e4, "\n\n" ;
?>
