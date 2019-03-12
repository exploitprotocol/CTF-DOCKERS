var browserWidth,browserHeight,requestAnimationFrame=window.requestAnimationFrame||window.mozRequestAnimationFrame||window.webkitRequestAnimationFrame||window.msRequestAnimationFrame,transforms=["transform","msTransform","webkitTransform","mozTransform","oTransform"],transformProperty=getSupportedPropertyName(transforms),snowflakes=[],numberOfSnowflakes=50,resetPosition=!1;function setup(){window.addEventListener("DOMContentLoaded",generateSnowflakes,!1),window.addEventListener("resize",setResetFlag,!1)}function getSupportedPropertyName(e){for(var t=0;t<e.length;t++)if(void 0!==document.body.style[e[t]])return e[t];return null}function Snowflake(e,t,o,n,s){this.element=e,this.radius=t,this.speed=o,this.xPos=n,this.yPos=s,this.counter=0,this.sign=Math.random()<.5?1:-1,this.element.style.opacity=.1+Math.random(),this.element.style.fontSize=12+32*Math.random()+"px"}function setTranslate3DTransform(e,t,o){var n="translate3d("+t+"px, "+o+"px, 0)";e.style[transformProperty]=n}function generateSnowflakes(){var e=document.querySelector(".snowflake"),t=e.parentNode;browserWidth=document.documentElement.clientWidth,browserHeight=document.documentElement.clientHeight;for(var o=0;o<numberOfSnowflakes;o++){var n=e.cloneNode(!0);t.appendChild(n);var s=getPosition(50,browserWidth),r=getPosition(50,browserHeight),i=5+40*Math.random(),a=new Snowflake(n,4+10*Math.random(),i,s,r);snowflakes.push(a)}t.removeChild(e),moveSnowflakes()}function moveSnowflakes(){for(var e=0;e<snowflakes.length;e++){(t=snowflakes[e]).update()}if(resetPosition){browserWidth=document.documentElement.clientWidth,browserHeight=document.documentElement.clientHeight;for(e=0;e<snowflakes.length;e++){var t;(t=snowflakes[e]).xPos=getPosition(50,browserWidth),t.yPos=getPosition(50,browserHeight)}resetPosition=!1}requestAnimationFrame(moveSnowflakes)}function getPosition(e,t){return Math.round(-1*e+Math.random()*(t+2*e))}function setResetFlag(e){resetPosition=!0}setup(),Snowflake.prototype.update=function(){this.counter+=this.speed/5e3,this.xPos+=this.sign*this.speed*Math.cos(this.counter)/40,this.yPos+=Math.sin(this.counter)/40+this.speed/30,setTranslate3DTransform(this.element,Math.round(this.xPos),Math.round(this.yPos)),this.yPos>browserHeight&&(this.yPos=-50)};