<script>
  import { exioCheckbox } from 'exio/svelte';
  import ShowingTags from './ShowingTags.svelte';
  import FullScreenImage from './FullScreenImage.svelte';

  /**
   * @type {boolean}
   */
  let show_start_message;
  /**
   * @type {boolean}
   */
  let no_img_found;
  /**
   * @type {string[]}
   */
  let filtered_tags = [];
  /**
   * @type {{ alt: string; src: string; original_path: string; tags: string[]; time: (string | number)[]; hv: boolean; }[]}
   */
  let filtered_img = [];
  let show_full_img = false;
  let full_screen_path = "";

  /**
   * @param {string} img_path
   */
  function enterFullScreen(img_path) {
    show_full_img = true;
    full_screen_path = img_path.slice(0,-4)+"jpg";
    console.log(full_screen_path)
  }

  function exitFullScreen() {
    show_full_img = false;
  }
</script>
{#if show_full_img}
<button  on:click={exitFullScreen}>exit</button>
<img class="fullscreen" src={full_screen_path} alt="something">
{:else}


<main style="margin: 0px, padding: 0px">
  <p class="lastupdatetime">This page was last updated on Sep 29, 2022.</p>
  <h2 style="padding-bottom: 10px">HELENA SU PHOTOGRAPHY</h2>

  <br />
  
  <ShowingTags
    bind:filtered_img
    bind:filtered_tags
    bind:show_start_message
    bind:no_img_found
  />

  {#if show_start_message}
    <p>please select as least one tag.</p>
  {/if}

  {#if no_img_found}
    <p>No photos are found!!!!</p>
  {/if}

  <div class="flex-container">
    {#each filtered_img as a_photo}
      <!-- svelte-ignore a11y-missing-attribute -->
      <div class="flex-items">
        {#if a_photo.hv}
          <img {...a_photo} style="width:600px" on:click={() => enterFullScreen(a_photo.src)}/>
        {:else}
          <img {...a_photo} style="height:500px" on:click={() => enterFullScreen(a_photo.src)} />
        {/if}
      </div>
    {/each}
  </div>
</main>
{/if}
<style>
  main {
    /* text-align: center; */
    padding: 1em;
    /* max-width: 240px; */
    /* background-color: beige; */
  }
  .lastupdatetime {
    color: #464d4f;
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
    font-family: 'Tapestry', cursive;

    letter-spacing: 3px;
    font-size: 4rem;
    margin: 0px;
    margin-left: 10px;
    text-align: left;
    color: #464d4f;
    font-stretch: condensed;
  }

  @media screen and (max-width: 600px) {
    h2 {
      font-size: 2.25rem;
      text-align: center;
    }
  }

  p {
    font-family: 'Piazzolla', serif;
    color: #d9dbca;
    font-size: 1.25rem;
    margin: 10px;
  }

  .checkbox-format {
    display: inline-flex;
    border-color: #919cbf;
  }
  .checkbox-format:hover {
    --exio-hover-border-color: white;
  }

  @media screen and (max-width: 600px) {
  }

  .fullscreen{
    max-width: 80%;
    max-height: 100%;

  }

  img {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  @media screen and (max-width: 600px) {
    img {
      max-width: 100%;
      max-height: 25rem;
      object-fit: contain;
    }
  }
  

  .flex-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    margin-bottom: 0px;
  }

  .flex-items {
    padding: 10px; /* this */
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
