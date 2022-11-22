<template>
    <div class="signup">
      <h1>Signup page</h1>
      <input type="text" placeholder="Email" id="emailInputID"/>
        <br>
        <br>
        <input type="text" placeholder="Password" id="passwdInputID"/>
        <br>
        <br>
      <button @click="signup">Signup</button>
    </div>
</template>

<script>
  export default {  
  name: 'Signup',
    data(){
      return {
        message: 'You have now signed up'
      }
    },
      methods: {
      signup(){
        alert(this.message)
      }
    }
  }
</script>
