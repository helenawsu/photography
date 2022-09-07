<script>
  //import { photos } from './create_img.js';
  // import { all_tags } from "./create_img.js";
  const photos = [
    {
      alt: 'Trekking',
      src: './photos/IMG_2043.webp',
      original_path: '',
      tags: ['Landscape', 'Europe'],
      time: [2022, 'July', ''],
    },
    {
      alt: 'Melting Origin',
      src: './photos/IMG_2176.webp',
      original_path: '',
      tags: ['Landscape', 'Europe'],
      time: [2022, 'July', ''],
    },
    {
      alt: 'A sheep meh like cow',
      src: './photos/IMG_2214.webp',
      original_path: '',
      tags: ['Animal', 'Europe'],
      time: [2022, 'July', ''],
    },
  ];

  var show_animal = 'Animal';
  var show_landscape = 'Landscape';
  var show_europe = 'Europe';
  var all_tags = [show_animal, show_landscape, show_europe];
  var show_start_message = true;
  var no_img_found = false;


  /**
* @type {string | any[]}
*/
  var filtered_tags= [];
  /**
   * @type {any[]}
   */
  var filtered_img = [];
  /**
* @param {string | any[]} filtered_tags
*/
  
  function refresh(filtered_tags) {
    filtered_img = [];

    for (var m = 0; m < photos.length; m++) {
      var add;
      if (filtered_tags.length>0){
        add = true;
        show_start_message=false;
      }
      else {
        show_start_message=true;
        add=false;
      }

      for (var n = 0; n < filtered_tags.length; n++) {

        if (!photos[m].tags.includes(filtered_tags[n])) {
          add = false;
        }
      }
      if (add) {
        filtered_img.push(photos[m]);
      }
    }
    if ((filtered_img.length==0) && (!show_start_message)){
      no_img_found = true;
    }

    console.log(filtered_img);
    return filtered_img;
  }
  $: filtered_img = refresh(filtered_tags);
</script>

<main>
  <p class="lastupdatetime">This page was last updated on Sep 6, 2022.</p>
  <h2 style="padding-bottom: 10px">Helena Su's Photos</h2>

  <br />

  <div class="flex-container">
    {#each all_tags as a_tag}
      <div class="flex-items">
        <label>
          <input
            type="checkbox"
            bind:group={filtered_tags}
            name="filtered tags"
            value={a_tag}
          />
          {a_tag}
        </label>
      </div>
    {/each}
  </div>
  

  {#if show_start_message}
    <p>please select as least one tag.</p>
  {/if}

  {#if no_img_found}
  <p>No photos are found!!!!</p>
{/if}



  {#each filtered_img as a_photo}
    <!-- svelte-ignore a11y-missing-attribute -->
    <img {...a_photo}/>
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
