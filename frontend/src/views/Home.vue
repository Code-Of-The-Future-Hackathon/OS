
<template>
    <div class="h-screen w-screen flex flex-col justify-center items-center relative">
        <div class="left-0 top-0 absolute z-[-1] after:content-[''] after:w-full after:h-full after:absolute after:bg-[#00000070] after:z-10 after:top-0 after:left-0">
            <video src="/public/landing-video.mp4" loop autoplay muted class="w-screen"></video>
        </div>

        <div class="flex items-center flex-col gap-4 w-1/2 text-white">
            <h1 class="font-bold text-8xl">OS</h1>
            <p class="w-1/2 text-center text-xl">natural disaster prediction maps </p>
        </div>
    </div>

    <div class="bg-[#1E1E1E] flex flex-col items-center relative z-10">
        <img src="/public/bg-blob-one.png" class="absolute z-0 select-none top-0 right-0 h-full" draggable="false" alt="">
        
       <div class="bg-[#00E2B9] z-10 w-1/2 h-1/3 rounded-[30px] border-2 border-[#1E1E1E] mt-36 p-10 justify-center items-center">
            <div class="flex">
                <h1 class="text-5xl font-bold w-full break-words">NATURAL DISASTER PREDICTION MAPS</h1>

                <div class="flex items-center justify-center flex-col text-center w-full gap-4">
                    <p>Real time based natural disaster prediction maps. Choose a disaster by layers</p>
                    <button @click="goToMap" class="bg-[#E9E3DC] hover:scale-105 active:scale-100 duration-100 px-6 font-bold shadow-sm shadow-black py-1 border-2 border-[#1E1E1E]">MAPS</button>
                </div>
            </div>
       </div> 

       <h1 class="bg-clip-text text-transparent font-bold text-5xl my-32 bg-gradient-to-r from-[#1CC357] z-10 to-[#0090B0]">OUT IDEA</h1>

       
       <div class="bg-[#02013233] w-2/5 h-1/2 p-2 relative rounded-[30px] flex justify-center flex-col items-center z-10">      

            <div class="w-full h-4 flex relative my-4 rounded-[30px] justify-center items-center">
                <div class="flex gap-3 absolute left-5 max-w-fit">
                    <span class="w-4 h-4 inline-block rounded-full bg-red-500"></span> 
                    <span class="w-4 h-4 inline-block rounded-full bg-yellow-500"></span> 
                    <span class="w-4 h-4 inline-block rounded-full bg-green-500"></span> 
                </div>
            </div>

            <div class="bg-[#57CC99] gap-12 w-[97%] h-[97%] py-4 rounded-[25px] flex flex-col justify-center items-center font-black text-[#1E1E1E] text-6xl pt-14 text-center">
               <h1 class="text-4xl w-64 break-word text-center"> NATURAL DISASTER PREDICTION </h1>
               <div class="flex flex-col gap-4 font-white">
                    <p class="text-xl font-thin w-[25ch]">Our idea is to predict natural disaster  possibility based on weather data API such as... </p>
                    <p class="text-xl font-thin w-[25ch]">rainfall,  rivers, snowfall, wind, temperature, soil and others.</p>
                    <p class="text-xl font-thin w-[25ch]">You can open our map and select a layer.</p>
                    <p class="text-xl font-thin w-[25ch]">Every layer is equivalent to a natural disaster. </p>
               </div>
            </div>
       </div>
    </div>

    <div class="h-screen bg-[#1E1E1E] flex items-center justify-center w-screen">
        <div class="w-1/2 z-10">
            <div class="flex flex-col gap-5">
                <h1 class="text-white text-6xl text-bold">Advantages</h1>
                <p class="text-white text-xl"> What are the advantages of our product? </p>
            </div>

            <div class="flex h-[70vh] gap-4 mt-16 text-center">
                <div class="flex h-full gap-4 flex-col w-full">
                    <div class="h-2/3 w-full bg-[#00E2B9] rounded-[40px] flex justify-center items-center">
                        <div>
                            <h1 class="text-3xl text-center font-bold"> Mindfulnes </h1>
                            <p class="w-26 p-8 text-xl"> OS promotes easier and mindful lifestyle. It is useful the same way as for business owners who specialize in the agriculture field as well as for the ordinary person. </p>
                        </div>
                    </div>
                    <div class="h-1/3 w-full bg-[#007C74] pt-6 text-white rounded-[40px] flex justify-center items-center">
                        <div>
                            <h1 class="text-3xl text-center font-bold"> AVAILABILITY </h1>
                            <p class="w-26 p-8 text-xl"> OS is a helpful website. It is also completely free to the public. </p>
                        </div>
                    </div>
                </div>
                <div class="flex h-full gap-4 flex-col w-full">
                    <div class="h-1/3 w-full bg-[#007C74] text-white pt-6 rounded-[40px] flex justify-center items-center">
                        <div>
                            <h1 class="text-3xl text-center font-bold"> PROBABILITY </h1>
                            <p class="w-26 p-8 text-xl"> OS do not guarantee a 100% true prognosis but a high enough probability. </p>
                        </div>
                    </div>

                    <div class="h-2/3 w-full bg-[#00E2B9] rounded-[40px] flex justify-center items-center">
                        <div>
                            <h1 class="text-3xl text-center font-bold"> KNOWLEDGE </h1>
                            <p class="w-26 p-8 text-xl"> OS gives you a lot new knowledge. It opens you doors to understand a teritory better. </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

const goToMap = () => {
    window.location.href = '/map';
}

</script>