<script>
  //import { photos } from './create_img.js';
  // import { all_tags } from "./create_img.js";
  const photos = [
    {
      title: 'Trekking',
      path: './photos/IMG_2043.webp',
      original_path: '',
      tags: ['Landscape', 'Europe'],
      time: [2022, 'July', ''],
    },
    {
      title: 'Melting Origin',
      path: './photos/IMG_2176.webp',
      original_path: '',
      tags: ['Landscape', 'Europe'],
      time: [2022, 'July', ''],
    },
    {
      title: 'A sheep meh like cow',
      path: './photos/IMG_2214.webp',
      original_path: '',
      tags: ['Animal', 'Europe'],
      time: [2022, 'July', ''],
    },
  ];

  var show_animal = {
    bool: false,
    name: 'Animal',
  };
  var show_landscape = {
    bool: false,
    name: 'Landscape',
  };
  var show_europe = {
    bool: false,
    name: 'Europe',
  };

  /**
   * @type {any[]}
   */
  var filtered_tags = [];
  /**
   * @type {any[]}
   */
  var filtered_img = [];
  /**
   * @type {string[]}
   */
  var filtered_tag_names = [];
  function refresh_tags() {
    filtered_tags = [];
    filtered_tag_names = [];
    var all_tags = [show_animal, show_landscape, show_europe];

    console.log(show_animal.bool);
    for (var m = 0; m < all_tags.length; m++) {
      console.log(all_tags[m]);
      if (all_tags[m].bool){
        filtered_tags.push(all_tags[m]); 
        console.log("adding somehting");
      }
      console.log(filtered_tags);

    }

    for (var i = 0; i < filtered_tags.length; i++) {
      filtered_tag_names.push(filtered_tags[i].name);
    }

    console.log(filtered_tags);
    for (var k = 0; k < photos.length; k++) {
      var this_tags = photos[k].tags;

      var add = true;
      for (var j = 0; j < filtered_tag_names.length; j++) {
        // @ts-ignore
        if (!this_tags.includes(filtered_tag_names[j])) {
          console.log(filtered_tag_names);
          add = false;
          console.log("this is false");
        }

        //Do something
      }
      if (add) {
        filtered_img.push(photos[k]);
        console.log("final", filtered_img);
      }
    }
  }
</script>

<main>
  <p class="lastupdatetime">This page was last updated on Sep 5, 2022.</p>
  <h2 style="padding-bottom: 10px">Helena Su's Photos</h2>
  <div class="flex-container">
    <div class="flex-items">
      <label>
        <input
          type="checkbox"
          bind:checked={show_landscape.bool}
          on:click={refresh_tags}
        />
        Landscape
      </label>
    </div>
    <div class="flex-items">
      <label>
        <input
          type="checkbox"
          bind:checked={show_animal.bool}
          on:click={refresh_tags}
        />
        Animal
      </label>
    </div>
    <div class="flex-items">
      <label>
        <input
          type="checkbox"
          bind:checked={show_europe.bool}
          on:click={refresh_tags}
        />
        Europe
      </label>
    </div>
  </div>

  <br />

  {#each filtered_img as { title, path, original_path, tags, time }}
    <img src="path," alt="title" />
    <p>show stuff</p>
  {/each}
</main>

<style>
  main {
    /* text-align: center; */
    padding: 1em;
    /* max-width: 240px; */
  }
  .lastupdatetime {
    color: #bbc3c7;
    margin-left: 10px;
    margin-top: 0px;
    text-align: right;
    /* line-height: 1rem; */
    /* font-family: 'Didact Gothic', sans-serif; */
  }

  @media screen and (max-width: 600px) {
    .lastupdatetime {
      font-size: 1rem;
      text-align: center;
      /* width:fit-content; */
    }
  }

  /* h1 {
    color: #ff3e00;
    font-family: 'Bodoni Moda', serif;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  } */
  h2 {
    font-family: 'Bodoni Moda', serif;
    font-size: 5rem;
    margin: 0px;
    margin-top: 15px;
    text-align: left;
  }

  /* @media screen and (min-width: 601px) {
  h2 {
    font-size: 5rem;
  }
} */

  @media screen and (max-width: 600px) {
    h2 {
      font-size: 2.5rem;
      text-align: center;
    }
  }

  /* h3{
    font-family: 'Aboreto', cursive;
    font-size: 1.5rem;
  }
  h4{
    font-family: 'Fraunces', serif;
    font-size: 1.5rem;
  } */
  p {
    font-family: 'Piazzolla', serif;
    color: #233b4d;
    font-size: 1.25rem;
  }
  label {
    font-family: 'Texturina', serif;
    font-size: 1.5rem;
    background-color: beige;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 5px;
    width: fit-content;
    margin-right: 10px;
  }

  .flex-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    margin-bottom: 20px;
  }

  .flex-items {
    padding: 0px; /* this */
    /* width: min-content; */
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
