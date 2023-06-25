<script setup>
import TaskItem from '../components/TaskItem.vue';
</script>

<style>
/* For mobile phones: */

h1{
  font-family: "Trirong", serif;
}

.center{
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.spacer {
  height: 100vh;
  width: 100%;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}

.layer1{
  background-image: url('../assets/layered-waves-haikei (1).svg');
}

  .responsiveWidth{
    width: 95%;
    margin:auto;
  }

  .circle{
    padding-right: 10px;
  }

  [class*="col-"] {
    width: 100%;
  }
 
  .round{
    border-radius: 10px
  }
  .inputField{
    border: none;
    width: 90%;
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 5px;
    padding-top: 8px;
  }
  input:focus, input:focus{
    outline: none;
}


  .wrapper:hover{
    color:white;
    transition: 0.5s;
    transform: rotateZ(-90deg);
  }
  .wrapper{
    color: gray;
    transition: 0.9s;
    transform: rotateZ(45deg);
  }
 

  .secondaryBtn{
    text-decoration: none;
    cursor: pointer;
    color: gray;
  }
  .secondaryBtn:hover{
    color:darkcyan;
  }

  @media screen and (min-width: 576px) {
    /* For desktop: */
    .layer1{
      background-image: url('../assets/layered-waves-haikei.svg');
    }
    .col-1 {width: 8.33%;}
    .col-2 {width: 16.66%;}
    .col-3 {width: 25%;}
    .col-4 {width: 33.33%;}
    .col-5 {width: 41.66%;}
    .col-6 {width: 50%;}
    .col-7 {width: 58.33%;}
    .col-8 {width: 66.66%;}
    .col-9 {width: 75%;}
    .col-10 {width: 83.33%;}
    .col-11 {width: 91.66%;}
    .col-12 {width: 100%;}
  }

  @media screen and (min-width: 768px) {
    /* For desktop: */
    .round{border-radius: 10px;}
    .responsiveWidth{ width: 45%; margin:auto}
    .col-1 {width: 8.33%;}
    .col-2 {width: 16.66%;}
    .col-3 {width: 25%;}
    .col-4 {width: 33.33%;}
    .col-5 {width: 41.66%;}
    .col-6 {width: 50%;}
    .col-7 {width: 58.33%;}
    .col-8 {width: 66.66%;}
    .col-9 {width: 75%;}
    .col-10 {width: 83.33%;}
    .col-11 {width: 91.66%;}
    .col-12 {width: 100%;}
  }
</style>

<template>
    <div class="spacer layer1" style="z-index:-1;width: 100%; position:fixed; top:0px;">
    </div>  
    <div class="responsiveWidth round text-white" style="background-color: rgb(150, 150, 147); margin-top:70px" >
      
        <div class="rounded-top" style="background-color: rgb(90, 87, 87);">
            <p class="border-bottom text-center" style="">Monday</p>
        </div>
        <TaskItem message="fdsjfkl"></TaskItem>
        <TaskItem message="fdsjfkl"></TaskItem>
        <TaskItem message="fdsjfkl"></TaskItem>
        
        <div>
            <p class="border-bottom text-center" style="background-color: rgb(90, 87, 87);">tuedday</p>
        </div>
        <TaskItem message="fdsjfkl"></TaskItem>
        <div>
            <p class="border-bottom text-center" style="background-color: rgb(90, 87, 87);">wednesday</p>
        </div>
        <TaskItem message="fdsjfkl"></TaskItem>
        <TaskItem message="fdsjfkl"></TaskItem>
        <div>
            <p class="border-bottom text-center" style="background-color: rgb(90, 87, 87);">Monday</p>
        </div>
        <TaskItem message="fdsjfkl"></TaskItem>
        <TaskItem message="fdsjfkl"></TaskItem>
        <TaskItem message="fdsjfkl"></TaskItem>
    </div>

</template>
