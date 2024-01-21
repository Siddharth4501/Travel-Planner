function Contactopenpopup()
{
    document.getElementById("contact-popupContainer").style.display='block';
    document.getElementById("contact-overlay").style.display='block';

}
function Contactclosepopup()
{
    document.getElementById("contact-popupContainer").style.display='none';
    document.getElementById("contact-overlay").style.display='none';

}

/****carausel js */

const slides=document.querySelectorAll(".slide")
var counter=0;
console.log(slides)

slides.forEach(
    (slide,index)=>{
        slide.style.left=`${index*100}%`
    }
)


const goNext=()=>{
    if(counter==slides.length-1){
        counter=0;
        
        slideImage();
        
    }
    else{
        counter++;
        slideImage();
    }
}
const goPrev=()=>{
    if(counter==0){
        counter=slide.length-1;
        
        slideImage();
    }
    else{
        counter--;
        slideImage();
    }
}


const slideImage=()=>{
    slides.forEach(
        (slide)=>{
            slide.style.transform=`translateX(-${counter*100}%)`
        }
    )
}
