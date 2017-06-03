#!/bin/sh
curl -vL http://q21.ctf.katsudon.org/ 2>&1 | awk '
    $2 != "X-Flag:"{
      next
    }
    s == $3{
      exit
    }
    s == ""{
      s=$3
    }
    {
      gsub(/\r/,"",$3);printf $3
    }
    END{
      print""
    }
'
