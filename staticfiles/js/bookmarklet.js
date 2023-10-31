const siteUrl = '//mysite.com:8000/';
const styleUrl = siteUrl + 'static/css/bookmarklet.css';


// load CSS
var head = document.getElementsByTagName('head')[0];
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random()*9999999999999999);
head.appendChild(link);


// load HTML
var body = document.getElementsByTagName('body')[0];
boxHtml = `
<div id="bookmarklet">
    <a href="#" id="close">&times;</a>
    <h1>Select an image to bookmark:</h1>
    <div class="images"></div>
</div>
`;
body.innerHTML += boxHtml


function bookmarkletlaunch(){
    bookmarklet = document.getElementById('bookmarklet');
    var imagesFound = bookmarklet.querySelector('.images');

    // clear images found
    imagesFound.innerHTML = '';
    // display bookmarklet
    bookmarklet.style.display = 'block';

    // close event
    bookmarklet.querySelector('#close').addEventListener('click', function(){
        bookmarklet.style.display = 'none';
    });

    // find images in the DOM
    images = document.querySelectorAll('img');
    images.forEach(image => {
            src = image.src
            result = src.indexOf('jpg') + src.indexOf('jpeg') + src.indexOf('png')
            if (result > 0){
                var imageFound = document.createElement('img');
                imageFound.src = src;
                imagesFound.append(imageFound)
            }
    })

    imagesFound.querySelectorAll('img').forEach(image => {
        image.addEventListener('click',function(event){
            imageSelected = event.target;
            bookmarklet.style.display = 'none';
            window.open(siteUrl + 'images/create/?url='
            + encodeURIComponent(imageSelected.src)
            + '&title='
            + encodeURIComponent(document.title),
            '_blank');
        })
    })
}

bookmarkletlaunch();
