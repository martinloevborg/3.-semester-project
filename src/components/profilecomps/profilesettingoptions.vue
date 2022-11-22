<template>
  <div class="grid_container">

    <div class="grid_column">
      <div id="ui_header">Edit Profile</div>
      <div class="ui_segment">
        <form class="ui_form" v-on:click.prevent.self>
          Edit personal information
          <div class="field">
            <div class="inputwrapper">
              <div class="labeler">First Name</div>
              <input type="text" name="fname" v-model="fname" v-validate="'required'" id="epInput">
            </div>

            <div class="inputwrapper">
              <div class="labeler">Last Name</div>
              <input type="text" name="lname" v-model="lname" v-validate="'required'" id="epInput">
            </div>
          </div>

          <div class="field">
            <div class="inputwrapper">
              <div class="labeler">Email</div>
              <input type="email" name="email" v-model="email" v-validate="'required|email'" placeholder="Email" id="epInput">
            </div>
          </div>

          <BirthdayOptions/>

          <div class="ui_segment2">
            Change password
            <div class="field2">
              <div class="inputwrapper">
                <div class="labeler">Current password</div>
                <input v-validate="'required'" name="password_current" type="password" placeholder="Password" ref="password-update" id="epInput">
              </div>
            </div>

            <div class="field2">
              <div class="inputwrapper">
                <div class="labeler">New password</div>
                <input v-validate="'required'" name="password" type="password" placeholder="Password" ref="password-update" id="epInput">
              </div>
            </div>

            <div class="field2">
              <div class="inputwrapper">
                <div class="labeler">Repeat new password</div>
                <input v-validate="'required|confirmed:password'" name="password_confirm" type="password" placeholder="Repeat Password" data-vv-as="password-update" id="epInput">
              </div>
            </div>
          </div>

          <div class="epButtons">
            <div class="inputwrapper3">
              <button id="dButton">Cancel</button>
            </div>
            <div class="inputwrapper2">
              <button type="submit" value="Submit">Save Profile</button>
            </div>
            <div class="inputwrapper3">
              <button id="dButton">Delete Profile</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import BirthdayOptions from '@/components/profilecomps/settingscomps/birthdayoptions.vue'

export default {
  name: 'EditProfileOptions',
  components: {
    BirthdayOptions
  },
  data () {
    return {
    };
  },
}
</script>