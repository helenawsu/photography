<script>
  import { exioCheckbox } from 'exio/svelte';
  import { photos, other_collapsible_tags, misc_tags } from './create_img.js';
  import {show_start_msg} from './store.js';

  /** @type {string[]}*/
  export let filtered_tags = [];

  let collapsible_tags = other_collapsible_tags;
  export let no_img_found = false;

  export let filtered_img = [];

  /** @param {number} num */
  function collapse(num) {
    show_start_msg.set(false);
    let bo = collapsible_tags[num].collapsed;
    collapsible_tags = [
      ...collapsible_tags.slice(0, num),
      {
        name: collapsible_tags[num].name,
        collapsed: !bo,
        tags: collapsible_tags[num].tags,
      },
      ...collapsible_tags.slice(num + 1, collapsible_tags.length),
    ];
  }

  /** @returns { { alt: string; src: string; original_path: string;
   * tags: string[]; time: (string | number)[]; hv: boolean; }[]}
   * @param {string[]} filtered_tags_param */
  function refresh(filtered_tags_param) {
    filtered_img = [];
    if (filtered_tags_param.includes('All')) {
      filtered_img = photos;
      return filtered_img;
    }
    if (filtered_tags_param.length === 0) {
      filtered_img = [
        {
          alt: '',
          src: '',
          original_path: '',
          tags: [''],
          time: [''],
          hv: true,
        },
      ];
    } else {
      filtered_img = photos.filter((photo) =>
        filtered_tags.every((tag) => photo.tags.includes(tag))
      );
    }
    no_img_found = filtered_img.length === 0 && filtered_tags_param.length > 0;

    return filtered_img;
  }

  /**
   * @param {string[]} filtered_tags
   */
  /**
   * @type {{ alt: string; src: string; original_path: string;
   * tags: string[]; time: (string | number)[]; hv: boolean; }[]}
   */
  $: filtered_img = refresh(filtered_tags);
</script>

<div class="flex-container" style="position: relative; top: 0px;">
  {#each misc_tags as misc_tag}
    <div style="" class="flex-items tag_groups">
      <label>
        <span>{misc_tag}</span>
        <input
          class="checkbox-format"
          type="checkbox"
          use:exioCheckbox
          bind:group={filtered_tags}
          name="filtered tags"
          value={misc_tag}
        />
      </label>
    </div>
  {/each}
</div>

<div class="flex-container">
  
  {#each collapsible_tags as tag_group, num}
  <div class = "tag_groups" style="">
  <div class="flex-items">
  <button  on:click={() => collapse(num)}>
    <h4>{tag_group.name}</h4></button
  ></div>
    {#each tag_group.tags.slice(0, !tag_group.collapsed ? tag_group.tags.length : 2) as a_tag,index}
      

      <div class="flex-items">
          <label>
            <span>
              {tag_group.tags[index]}
            </span>
            <input
              class="checkbox-format"
              type="checkbox"
              use:exioCheckbox
              bind:group={filtered_tags}
              name="filtered tags"
              value={tag_group.tags[index]}
            />
          </label>
      </div>
      <div />
    {/each}
  </div>
  {/each}
</div>

<style>
  h4 {
    font-family: 'Inknut Antiqua', serif;
    font-size: 1.5rem;
    color: #d9dbca;
    margin: 0;
    padding:0;
    padding-left: 10px;
    padding-right: 10px;
    line-height: normal;
    display: block;
    height: 100%;
    border-left: #a89732 5px solid;
  }
  @media screen and (max-width: 600px) {
    h4 {
      max-width: 100%;
      font-size: 1.25rem;

    }
  }

  input {
    vertical-align: middle;
    position: relative;
    margin-right: 20px;
  }
  @media screen and (max-width: 600px) {
    input {
      margin-right: 10px;

    }
  }
   button {
    background-color: #0f0f19;
    font-family: 'Inknut Antiqua', serif;
    border: none;
    margin: 0px;
    padding: 0px;
    color:white;
    padding-left: 5px;
    padding-top: 5px;
    padding-bottom: 5px;
   }

  button:hover {
    background-color: #464d4f;
  } 
  button:active {
    background-color: #464d4f;
  } 

  span {
    vertical-align: middle;
    position: relative;
    bottom:3px;
  }

  .checkbox-format {
    display: inline-flex;
    border-color: #919cbf;
    vertical-align: -webkit-baseline-middle;
    /* margin:0; */
    margin-right:0;
    padding:0;
  }
  .checkbox-format:hover {
    --exio-hover-border-color: white;
  }

  @media screen and (max-width: 600px) {
  }

  label {
    font-family: 'Texturina', serif;
    font-size: 1.5rem;
    /* background-image: linear-gradient
    (to left, rgba(255, 217, 0, 0.43) , rgba(145, 156, 191, 0.43)); */
    margin-left: 0px;
    margin-right:0px;
    padding-right: 0px;
    padding-left: 15px;
    color: #d9dbca;
    /* display: inline-flex; */
    border-left: solid #a89732 0.5px;
    display: block;
  }
  @media screen and (max-width: 600px) {
    label {
      font-size: 1.25rem;
      padding-left: 5px;
      margin-left:5px;

    }
  }

  .flex-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    margin-bottom: 0px;
  }
  @media screen and (max-width: 600px) {
    .flex-container {
      max-width: 100%;
      flex-wrap: wrap;
    }
  }
  .flex-items {
    padding: 10px; /* sthis */
    align-items: center;
    display: flex;
    flex-direction: row;
  }
  @media screen and (max-width: 600px) {
    .flex-items {
      padding:5px;
    }
  }
 .tag_groups {
  display:flex; background-color: #232421; padding: 5px; margin: 5px;
 }
 @media screen and (max-width: 600px) {
    .tag_groups {
      max-width: fit-content;
      padding: 5px;
      margin: 5px;
      flex-wrap: wrap;
      display:inline-block;

    }
  }

</style>
