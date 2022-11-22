<template>
  <div id=addSong>
    <div class="addSong">
      
      <h1>Youtube data stealer</h1>
      <input class="form-control" v-on:keyup.enter="submit" readonly="rOnly" id='link' ref="link" placeholder="Youtube Link"
        value="https://www.youtube.com/watch?v=HgzGwKwLmgM"/>'
        
      <button id="linkButton" type="submit" v-if="isUploading" @click="isUploading = false, isSubmitting = true, rOnly = true">Upload</button>

      <p id="uploadConfirm"></p>

      <div class="grid_container" v-if="isSubmitting">
        <div class="grid_item">
      <img style="display: none;" id="thumbnailID" class="img-fluid" alt="Responsive image">
      <img src="@/assets/Random_Album_cover.jpg">
      </div>
      
      <div class="grid_item">
      <div id="meta-form">
      <div class="form-row">

      <div class="form-group col-md-6">
        <label for="Title">Title</label> <br>
        <input class="form-control" v-model="title" id="Title" placeholder="Title">
      </div><br>

      <div class="form-group col-md-6">
        <label for="Artist">Artist</label><br>
        <input class="form-control" v-model="artist" id="Artist" placeholder="Artist">
      </div><br>

      <div class="form-group col-md-6">
        <label for="ReleaseDate">Release Date</label><br>
        <input class="form-control" v-model="releasedate" id="ReleaseDate" placeholder="Release Date">
      </div><br>

      <div class="form-group col-md-6">
        <label for="Genre">Genre</label><br>
        <input class="form-control" v-model="genre" id="Genre" placeholder="Genre">
      </div><br>

      <div class="form-group col-md-6">
        <label for="Producer">Producer</label><br>
        <input class="form-control" v-model="producer" id="Producer" placeholder="Producer">
      </div><br>

      <div class="form-group col-md-6">
        <label for="Writers">Writers</label><br>
        <input class="form-control" v-model="writers" id="Writers" placeholder="Writers">
      </div><br>

      <div class="form-group col-md-6">
        <label for="Co-artist">Co-artist</label><br>
        <input class="form-control" v-model="coartist" id="CoArtist" placeholder="Co-artist">
      </div><br>

      <div class="form-group col-md-6">
        <label for="Album"> Album </label><br>
        <input class="form-control" v-model="album" id="Album" placeholder="Album">
      </div><br>

      <div class="form-group col-md-6">
        <label for="RecordLabel">Record Label</label><br>
        <input class="form-control" v-model="recordlabel" id="RecordLabel" placeholder="Record Label">
      </div><br>
      </div>
      </div>

    </div>
    </div>
    <div class="cabuttonwrapper" v-if="isSubmitting">
        <button class="cbutton" @click="cAddSong(), isUploading = true, isSubmitting = false, rOnly = false" type="button">Cancel</button>
        <button class="abutton" v-on:keyup.enter="submit" @click="submit = true" type="button">Submit</button>
      </div>
      </div>
  </div> 
</template>

<script>
export default {
  name: 'AddSong',
  data () {
    return {
      isUploading: true,
      isSubmitting: false,
      rOnly: false,
      title: '',
      artist: '',
      releasedate: '',
      genre: '',
      producer: '',
      writers: '',
      coartist: '',
      album: '',
      recordlabel: '',

    };
  },
  ready:function(){
    this.cAddSong();
  },
  methods: {
    cAddSong () {
      this.title = '';
      this.artist = '';
      this.releasedate = '';
      this.genre = '';
      this.producer = '';
      this.writers = '';
      this.coartist = '';
      this.album = '';
      this.recordlabel = '';
    }
  }
}

</script>

<style scoped>
.grid_container{
  display:grid ;
  grid-template-columns: 25% 25%;
  justify-content:center ;
  text-align: left;
  width: 80%;
  margin: auto;
}
input{
  width: 25em;
}
</style>