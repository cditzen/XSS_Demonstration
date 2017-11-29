function loadPosts() {
    document.getElementById("content_anchor").innerHTML = httpGet("http://127.0.0.1:8081/posts");
}

function submitPost() {
    var textArea = document.getElementById("compose_post_area");
    var postText = textArea.value;
    if (document.getElementById("SanitizeInput").checked) {
        postText = htmlEscape(postText);
    }
    textArea.value = "";

    httpPost("http://127.0.0.1:8081/submit-post", postText);
}

function clearDatabase() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "POST", "http://127.0.0.1:8081/clear-database", false);
    xmlHttp.send(null);
    if (xmlHttp.status == 200) {
        loadPosts();
    }
}

function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send(null);

    var obj = JSON.parse(xmlHttp.responseText);

    http = "";
    for (let i = 0; i < obj.length; i++) {
        http += "<div class=\"well\"><p>Post #" + (i + 1) + ":</p><p>" + obj[i] + "</p></div>";
    }
    return http;
}

function httpPost(theUrl, post) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "POST", theUrl, false);
    xmlHttp.send(post);
    if (xmlHttp.status = 200) {
        loadPosts();
    }
}

// Source: https://github.com/google/closure-library/blob/master/closure/goog/string/string.js#L541
// Very simplified version of Google's HtmlEscape function found
// in their Javascript closure library
function htmlEscape(str) {
    return str.replace(/&/g, '&amp;')
              .replace(/</g, '&lt;')
              .replace(/>/g, '&gt;')
              .replace(/\x00/g, '&#0;');
}