<script>
  import ShowingTags from './ShowingTags.svelte';
  import FullScreenImage from './FullScreenImage.svelte';
  import {
    focused_img,
    show_start_msg,
    show_full_img,
    current_scroll_position,
  } from './store.js';
  let c_scroll_position;
  /** @type {number} */
  let y;
  /**@type {boolean}*/
  let full_screen;
  /** @type {boolean}*/
  let show_start_message;
  /** @type {boolean}*/
  let no_img_found;
  /** @type {string[]}*/
  let filtered_tags = [];
  /** @type {{ alt: string; src: string; original_path: string;
   * tags: string[]; time: (string | number)[]; hv: boolean; rating: number}[]}*/
  let filtered_img = [];
  show_full_img.subscribe((value) => {
    full_screen = value;
  });
  current_scroll_position.subscribe((value) => {
    c_scroll_position = value;
  });

  /**
   * @param {{ alt: string; src: string; original_path: string; tags: string[];
   * time: (string | number)[]; hv: boolean; rating: number; }} img_param
   */
  function enterFullScreen(img_param) {
    show_full_img.set(true);
    focused_img.set(img_param);
    current_scroll_position.set(y);
  }
</script>

<svelte:window bind:scrollY={y} />

<main style="margin: 0px, padding: 0px">
  {#if $show_full_img}
    <FullScreenImage />
  {:else}
    <p class="lastupdatetime">This page was last updated on Oct 25, 2022.</p>
    <h1 style="padding-bottom: 10px">Helena Su Photograhpy</h1>

    <br />

    <ShowingTags bind:filtered_img bind:filtered_tags bind:no_img_found />

    {#if $show_start_msg}
      <br />
      <p>Click tag category for more tags!</p>
    {/if}

    {#if no_img_found}
      <p>No photos are found!!!!</p>
    {/if}

    <div class="flex-container">
      {#each filtered_img as a_photo}
        <div class="flex-items">
          {#if a_photo.hv}
            <!-- svelte-ignore a11y-missing-attribute -->
            <img
              class="img_hover"
              {...a_photo}
              style="width:600px"
              on:click={() => enterFullScreen(a_photo)}
            />
          {:else}
            <!-- svelte-ignore a11y-missing-attribute -->
            <img
              class="img_hover"
              {...a_photo}
              style="height:500px"
              on:click={() => enterFullScreen(a_photo)}
            />
          {/if}
        </div>
      {/each}
    </div>
  {/if}
</main>

<style>
  main {
    /* text-align: center; */
    padding: 1em;
    /* max-width: 240px; */
    /* background-color: beige; */
  }
  @media screen and (max-width: 600px) {
    main {
      padding: 0.25em;
    }
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

  h1 {
    font-family: 'Caudex', serif;
    letter-spacing: 3px;
    font-size: 3rem;
    margin: 0px;
    margin-left: 10px;
    text-align: left;
    color: #d9dbca;
    font-stretch: condensed;
  }
  @media screen and (max-width: 600px) {
    h1 {
      font-size: 2.25rem;
      text-align: center;
    }
  }

  p {
    font-family: 'Piazzolla', serif;
    color: #d9dbca;
    font-size: 1.25rem;
    margin: 20px;
  }
  .description {
    text-align: center;
    vertical-align: middle;
    align-self: center;
    padding-left: 20px;
    padding-right: 20px;
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
  .stretch_h {
    width: 70vw;
  }
  .stretch_v {
    height: 90vh;
  }
  .fullscreen {
    display: grid;
    align-content: center;
    position: relative;
  }
  .img_hover:hover {
    opacity: 0.5;
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
      border: none;
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
