<script>
  import { exioCheckbox } from 'exio/svelte';
  import { photos, other_collapsible_tags, misc_tags } from './create_img.js';

  /**
   * @type {string[]}
   */
  export let filtered_tags = [];

  let collapsible_tags = other_collapsible_tags;
  export let no_img_found = false;

  export let filtered_img = [];

  /**
   * @param {number} num
   */
  function collapse(num) {
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

  /**
   * @returns { { alt: string; src: string; original_path: string;
   * tags: string[]; time: (string | number)[]; hv: boolean; }[]}
   * @param {string[]} filtered_tags_param
   */
  function refresh(filtered_tags_param) {
    filtered_img = [];
    if (filtered_tags_param.includes('All')) {
      filtered_img = photos;
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
    <div class="flex-items">
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
    {#if tag_group.collapsed}
      <button class="" on:click={() => collapse(num)}>
        <h4>{tag_group.name}</h4></button
      >

      <div class="flex-items">
        {#each tag_group.tags.slice(0, 2) as a_tag, index}
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
        {/each}
      </div>
      <div />
    {:else}
      <button class="" on:click={() => collapse(num)}
        ><h4>{tag_group.name}</h4></button
      >
      <div class="flex-items">
        {#each tag_group.tags as a_tag}
          <label>
            <span>
              {a_tag}
            </span>
            <input
              class="checkbox-format"
              type="checkbox"
              use:exioCheckbox
              bind:group={filtered_tags}
              name="filtered tags"
              value={a_tag}
            />
          </label>
        {/each}
      </div>
      <div />
    {/if}
  {/each}
</div>

<style>
  h4 {
    font-family: 'Inknut Antiqua', serif;
    font-size: 1.5rem;
    color: #d9dbca;
    padding-left: 10px;
    margin: 0;
    padding: 0;
    display: block;
    height: 100%;
    font-family: 'Inknut Antiqua', serif;
    font-size: 1.5rem;
    color: #d9dbca;
  }
  input {
    vertical-align: middle;
    position: relative;
    margin-right: 20px;
  }
  button {
    background-color: #0f0f19;
    font-family: 'Inknut Antiqua', serif;
    border-right: none;
    border-bottom: none;
    border-left: none;
    border-top: none;

    padding-top: 0px;
    margin-right: 10px;
    margin-top: 10px;
  }
  button:hover {
    background-color: #464d4f;
  }

  span {
    top: 3px;
    transform: translateY(42px);
    vertical-align: top;
    position: relative;
  }

  .checkbox-format {
    display: inline-flex;
    border-color: #919cbf;
    vertical-align: -webkit-baseline-middle;
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
    padding-right: 0px;
    padding-left: 15px;
    display: block;
    color: #d9dbca;
    border-left: solid wheat 0.5px;
  }
  @media screen and (max-width: 600px) {
    label {
      font-size: 1.25rem;
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
</style>
