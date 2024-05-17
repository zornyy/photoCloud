import PocketBase from 'pocketbase';
import { writable } from 'svelte/store';

const PB_URL = "http://127.0.0.1:8090";
export const pb = new PocketBase(PB_URL);
export const user = writable(pb.authStore.model);

export default pb