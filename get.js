// curl -H 'Accept: application/json; indent=4' -u admin:Yuyu@123 http://127.0.0.1:8000/questions/

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

//"
//	{
//		"count":2,"next":null,"previous":null,
//      "results":[
//          {
//              "url":"http://127.0.0.1:8000/questions/1/",
//              "id":1,
//              "question_text":"que hora son?",
//              "pub_date":"2020-11-09T21:33:00Z"
//          },
//          {
//              "url":"http://127.0.0.1:8000/questions/2/",
//              "id":2,
//              "question_text":"como te llamas?",
//              "pub_date":"2020-11-09T21:33:00Z"
//          }
//      ]
//  }
//"