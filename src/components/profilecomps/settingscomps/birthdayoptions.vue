<template>
    <div class="field">
      <div class="inputwrapper">
          <div class="labeler">Day</div>
          <select @input="daySelected" type="number" v-model="day" id="day" v-validate="'required|day'">
              <option disabled value="">Day</option>
              <option v-for="dayOption in days" v-bind:key="dayOption.day">{{ dayOption }}</option>
          </select>
        </div>

        <div class="inputwrapper">
          <div class="labeler">Month</div>
          <select @input="monthSelected = true" type='text' v-model='month' v-on:change="updateDays" id="month">
              <option disabled value="">Month</option>
              <option v-for="monthOption in months" v-bind:key="monthOption.month">{{ monthOption }}</option>
          </select>
        </div>

        <div class="inputwrapper">
          <div class="labeler">Year</div>
          <select @input="yearSelected = true" type="number" v-model="year" v-on:change="updateDays" id="year">
              <option disabled value="">Year</option>
              <option v-for="yearOption in years" v-bind:key="yearOption.year">{{ yearOption }}</option>
          </select>
        </div>
    </div>
</template>

<script>
export default {
  name: 'BirthdayOptions',
  data () {
    return {
      days: [],
      months: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
      years: [],
      year: '',
      month: '',
      day: '',
      yearSelected: false,
      monthSelected: false,
      daySelected: false,
    };
  },
  /*
  Loads years, and days into input fields of birth day before component is loaded.
  Years loaded will be last 100 years from current year.
  */
  created (){
    this.loadYears();
    this.loadDays();
  },
  /*
  Updates 'days' array depending on month in year selected.
  Will not unselect picked day if the day exist in the updated array.
  */
  ready:function(){
    this.updateDays();
  },
  methods: {
    loadYears () {
      const yearObj = new Date().getFullYear();
      const yearIter = 100;
      for (let y = 0; y < yearIter; y++){
        const year = new Date(yearObj);
        this.years.push(year-y);
      }
    },
    loadDays () {
      for (let d = 0; d < 31; d++){
          this.days.push(d+1);
        }
    },
    updateDays () {
      if (this.yearSelected && this.monthSelected === true){
        this.days = [];
        const month = this.months.indexOf(this.month)+1;
        const lastDay = new Date(this.year, month, 0).getDate();
        for (let d = 0; d < lastDay; d++){
          this.days.push(d+1);
        }
      }
    },
  }
}
</script>