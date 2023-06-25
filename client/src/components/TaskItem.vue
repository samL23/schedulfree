<style>
  .task{
    cursor: pointer;
  }
  .done{
    text-decoration: line-through;
    color:gray
  }
</style>

<template>
    <p class=" task border-bottom"><i class="fa fa-circle-o circle" style="font-size:24px"></i>{{ message }}</p>
</template>

<script>
export default {
  props: ['message'],
};


</script>