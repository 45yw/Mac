var value = "あいうえおあいうえお" ;
var before = "う" ;
var regExp = new RegExp( before, "g" ) ;
var result = value.replace( regExp , "く" ) ;
