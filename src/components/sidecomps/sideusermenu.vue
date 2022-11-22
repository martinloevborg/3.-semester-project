<template>
    <div class="sideusermenu" @mouseover="hover = true, phover = false" @mouseleave="hover = false, phover = true">
        <router-link to="/profile" id="routing_main_user">
            <img class="userimg" :src='accImg'>
        </router-link>
        <div class ="userNameWrapper">
            <div class="username">
                <router-link to="/profile" id="routing_main_user">{{ accUserName }}</router-link>
                <div class="ddArrow">
                    <svg :class="{ rotate:phover }" width="7" height="4" viewBox="0 0 7 4" fill="none">
                        <path d="M1.03248 1.7825L2.97498 3.725C3.26748 4.0175 3.73998 4.0175 4.03248 3.725L5.97498 1.7825C6.44748 1.31 6.10998 0.5 5.44248 0.5H1.55748C0.889977 0.5 0.559978 1.31 1.03248 1.7825Z" fill="white"/>
                    </svg>
                    <div class="ddMenuTop" v-if="hover">
                        <svg class="ddBoxArrow" width="15" height="10" viewBox="0 0 15 10" fill="none">
                            <path d="M7.5 0L14.8612 9.75H0.138784L7.5 0Z" fill="#343030"/>
                        </svg>
                    </div>
                </div>
            </div>
        </div>
        <div class="ddWrapper" v-if="hover">
            <svg class="ddBoxMenu" width="131" height="122" viewBox="0 0 131 122" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect width="131" height="122" rx="6" fill="#292929"/>
                </svg>
            <span class="menu_directs">
                <div class="dd_item">
                    <router-link to="/account" id="ddrouting">Account</router-link>
                </div>
                <div class="dd_item">
                    <router-link to="/account/settings" id="ddrouting">Settings</router-link>
                </div>
                <div class="dd_item">
                    <router-link to="/" id="ddrouting">Log out</router-link>
                </div>
            </span>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SideUserMenu',
    data() {
        return {
            hover: false,
            phover: true,
            accUserName: "Jane Doe",
            accImg: require("@/assets/userMenuImg.png"),
        }
    },
}
</script>