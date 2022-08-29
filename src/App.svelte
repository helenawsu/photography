<script>
	let showLandscape = false;
  let showAnimal = false;

</script>

<main>
  <p class="lastupdatetime">
    This page was last updated on Aug 28, 2022.
  </p>
  <h2>PHOTOGRAPHY</h2>
  <div class="flex-container">
    <div class="flex-items">
      <label>
        <input type=checkbox bind:checked={showLandscape}>
        landscape
      </label>
    </div>
    <div class="flex-items">
      <label>
        <input type=checkbox bind:checked={showAnimal}>
        animal
      </label>
    </div>
  </div>
 
 
  <br>


  {#if showLandscape}
    <br>
    <img 
    src="./photos/IMG_2176.webp"
    width="500"
    alt="ice cave">
  {:else}
{/if}


{#if showAnimal}
    <img 
    src="./photos/IMG_2214.jpg"
    width="500"
    alt="ice cave">
{/if}
  <p>
    bruh this checkbox is so ugly
  </p>

</main>

<style>
  main {
    /* text-align: center; */
    padding: 1em;
    max-width: 240px;
  }
  .lastupdatetime {
    padding: 0rem;
    color: #bbc3c7;
    margin-right: 10px;
    margin-top: 0px;
    text-align: right;
    padding: 0;
    line-height: 1em;
    font-family: 'Didact Gothic', sans-serif;

  }
  h1 {
    color: #ff3e00;
    font-family: 'Bodoni Moda', serif;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;

   
  }
  h2 {
    font-family: 'Fraunces', serif;
    font-size: 5rem;
    margin: 0px;
    margin-top: 15px;
    text-align: center;
  }
  h3{
    font-family: 'Aboreto', cursive;
    font-size: 1.5rem;
  }
  h4{
    font-family: 'Fraunces', serif;
    font-size: 1.5rem;
  }
  p {
    font-family: 'Didact Gothic', sans-serif;
    color: #233b4d;
    font-size: 1.25rem;
  }
  label{
    font-family: 'Aboreto', cursive;
    font-size: 1.5rem;
    border: solid 1px;
    width: fit-content;}

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
