import { playlistURL } from "@/helpers/URLHelper"
//import { getToken } from "@/helpers/CookieHelper"

/**
 * 
 * @param {*} username 
 */
function getPlaylists(username){
    return fetch(playlistURL+username, {
        method: "GET",
        headers: new Headers({
            // 'Authorization': 'Bearer ' + getToken(),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }).then(res => {
        if (res.ok){
            return Promise.resolve(res.json())
        } else {
            return Promise.reject(new Error(res.json()))
        }
    })
}

/**
 * 
 * @param {*} playlistName 
 */
function getSongsInPlaylist(playlistName){
    return fetch(playlistURL+playlistName+"/songs", {
        method: "GET",
        headers: new Headers({
            // 'Authorization': 'Bearer ' + getToken(),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }).then(res => {
        if (res.ok){
            return Promise.resolve(res.json())
        } else {
            return Promise.reject(new Error(res.json()))
        }
    })
}

/**
 * 
 * @param {*} username 
 * @param {*} jsonPlaylist 
 */
function postPlaylist(username, jsonPlaylist){
    return fetch(playlistURL+'create/' + username, {
        method: "POST",
        headers: new Headers({
            // 'Authorization': 'Bearer ' + getToken(),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }),
        body: jsonPlaylist
    }).then(res => {
        if (res.ok){
            return Promise.resolve(res.json())
        } else {
            return Promise.reject(new Error(res.json()))
        }
    })
}

/**
 * 
 * @param {*} username 
 */
function deletePlaylist(username){
    return fetch(playlistURL+'delete/' + username, {
        method: "POST",
        headers: new Headers({
            // 'Authorization': 'Bearer ' + getToken(),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }),
        body: ""
    }).then(res => {
        if (res.ok){
            return Promise.resolve(res.json())
        } else {
            return Promise.reject(new Error(res.json()))
        }
    })
}

export const PlaylistService = {
    getPlaylists,
    getSongsInPlaylist,
    postPlaylist,
    deletePlaylist
}

