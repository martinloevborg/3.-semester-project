<template>
  <div class="forgotpasswd"> 
    <section>
      <br>
      <h1>Reset password?</h1>
      <br>
      <br>
      <pre>
        Enter your emial address that you used to
        register. We'll send you an email with your
        username and a link to reset your password
      </pre>  
      <br>
      <p style="margin-right: 11%">Email</p>
      <input type="text" placeholder="your@mail.com" id="forgotpasswd"/>
      <br>
      <br>
      <button @click="forgotpasswd" style="margin-right: 2%">Cancel</button>
      <button @click="forgotpasswd" style="margin-left: 2%">Send</button>
      <br>
      <br>
    </section>
  </div>
</template>

<script>

export default {
name: 'Forgotpasswd',
  data(){
    return {
      message: '200 ok'
    }
  },
    methods: {
    forgotpasswd(){
      alert(this.message)
    }
  }
}

</script>
