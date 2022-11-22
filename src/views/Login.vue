<template>
  <div class="login">
    <h1>Login page</h1>
    <form action="/action_page.php">
     <label for="email">E-mail</label><br>
     <input type="text" id="email" name="email"><br>
     <label for="passwd">Password</label><br>
     <input type="password" id="passwd" name="passwd"><br>
    </form> <br>
    <button @click="login">Login</button>
  </div>
</template>

<script>
import { LoginService } from '@/services/LoginService'

export default {  
name: 'Login',
    methods: {
        async login(){
        const email = document.getElementById("email").value;
        const passwd = document.getElementById("passwd").value; 
        const jsonUser = '{ "email":"' + email + '", "passwd":"' + passwd + '" }'

        await alert(LoginService.login(jsonUser));
        
    }
  }
}
</script>