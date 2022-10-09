<script>
  import ShowingTags from './ShowingTags.svelte';
  import { afterUpdate } from 'svelte';
  /**
   * @type {number}
   */
  let y;
  /**
   * @type {number}
   */
  let current_scroll_position = 0;

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
  let scroll = false;

  /**
   * @type {{ alt: string; src: string; original_path: string; tags: string[]; time: (string | number)[]; hv: boolean; }}
   */
  let focused_img = {
    alt: '',
    src: '',
    original_path: '',
    tags: [''],
    time: [''],
    hv: true,
  };

  /**
   * @param {{ alt: string; src: string; original_path: string; tags: string[]; time: (string | number)[]; hv: boolean; }} img_param
   */
  function enterFullScreen(img_param) {
    console.log("entering")

    show_full_img = true;
    focused_img = img_param;
    focused_img.original_path = img_param.src.slice(0, -4) + 'jpg';
    current_scroll_position = y;
  }

  function exitFullScreen() {
    show_full_img = false;
    scroll = true;
    console.log("exiting")
  }
  $: scroll &&
  setTimeout(() => {
      console.log('is it scrolling ', scroll);

      if (scroll) {window.scrollTo(0, current_scroll_position);
      console.log('scrolling', current_scroll_position);}

      scroll = false;
    },3);
//   $: show_full_img &&
// setTimeout(() => {
//     console.log('is it scrolling to top',show_full_img);

//     if (show_full_img) {window.scrollTo(0, 0);
//     console.log('scrolling', 0);}

//   },3);
</script>

<svelte:window bind:scrollY={y} />

<main style="margin: 0px, padding: 0px">
  {#if show_full_img}
    <button on:click={exitFullScreen}>exit</button>
    <p style="display: inline-block" class="fullscreenimg">{focused_img.alt}</p>

    <div class="fullscreen">
      {#if focused_img.hv}
        <img
          class="fullscreenimg_big_h"
          src={focused_img.original_path}
          alt={focused_img.alt}
        />
        <img
          class="fullscreenimg_small_h stretch_h"
          src={focused_img.src}
          alt={focused_img.alt}
        />
      {:else}
        <img
          class="fullscreenimg_big_v"
          src={focused_img.original_path}
          alt={focused_img.alt}
        />
        <img
          class="fullscreenimg_small_v stretch_v"
          src={focused_img.src}
          alt={focused_img.alt}
        />
      {/if}
    </div>
  {:else}
    <p class="lastupdatetime">This page was last updated on Oct 8, 2022.</p>
    <h1 style="padding-bottom: 10px">Helena Su Photograhpy</h1>

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
            <img
              class="img_hover"
              {...a_photo}
              style="width:600px"
              on:click={() => enterFullScreen(a_photo)}
            />
          {:else}
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
  h2 {
    font-family: 'Caudex', serif;

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
  h4 {
    font-family: 'Inknut Antiqua', serif;
    font-size: 1.5rem;
    color: white;
    padding-left: 10px;
    vertical-align: middle;
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
  .stretch_h {
    width: 70vw;
  }
  .stretch_v {
    height: 70vh;
  }
  .fullscreen {
    display: grid;
    align-content: center;
    position: relative;
  }
  .fullscreen > .fullscreenimg_big_h {
    grid-column: 1/-1;
    grid-row: 1/-1;
    z-index: -1;
    max-width: 70vw;
  }
  .fullscreen > .fullscreenimg_big_v {
    grid-column: 1/-1;
    grid-row: 1/-1;
    z-index: -1;
    max-height: 70vh;
  }
  .fullscreen > .fullscreenimg_small_h {
    grid-column: 1/-1;
    grid-row: 1/-1;
    z-index: -2;
  }
  .fullscreen > .fullscreenimg_small_v {
    grid-column: 1/-1;
    grid-row: 1/-1;
    z-index: -2;
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
