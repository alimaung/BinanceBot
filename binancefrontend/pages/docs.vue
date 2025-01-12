<template>
    <v-sheet class="area">
        <v-sheet class="sidebar">
            <v-list v-model:opened="open" class="sidebar-list">
                <v-list-item title="Documentation" class="sidebar-item"></v-list-item>
                <v-divider></v-divider>
                <v-list-item prepend-icon="mdi-information-outline" title="Changelog" link to="/changelog"></v-list-item>
                <v-list-item prepend-icon="mdi-text-box" title="Readme" link to="/readme"></v-list-item>
                <v-list-item prepend-icon="mdi-language-html5" title="Frontend" link to="/frontend"></v-list-item>
                <v-list-item prepend-icon="mdi-server" title="Backend" link to="/backend"></v-list-item>
                <v-list-item prepend-icon="mdi-cellphone" title="Mobile" link to="/mobile"></v-list-item>
                <v-list-group value="Changelog" fluid>
                    <template v-slot:activator="{ props }">
                        <v-list-item v-bind="props" prepend-icon="mdi-help-circle-outline" title="FAQs"></v-list-item>
                    </template>
                    <v-list-item v-bind="props" prepend-icon="mdi-key" title="API" link to="/api"></v-list-item>
                </v-list-group>
                <v-list-item v-bind="props" prepend-icon="mdi-currency-btc" title="Binance" link to="/binance"></v-list-item>
                <v-list-item v-bind="props" prepend-icon="mdi-currency-btc" title="placeholder" link to="/docs"></v-list-item>
            </v-list>
        </v-sheet>

        <v-btn 
            class="edit-btn" 
            :icon="isEditing ? 'mdi-content-save' : 'mdi-pencil'" 
            size="x-large" 
            color="#F0B90B" 
            @click="toggleEdit"
        ></v-btn>

        <v-sheet class="content">
            <div class="breadcrumbs">
                <v-breadcrumbs :items="items">
                    <template v-slot:divider>
                        <v-icon icon="mdi-chevron-right"></v-icon>
                    </template>
                </v-breadcrumbs>
            </div>
            <div class="doc">
                <TipTapEditor v-if="isEditing" v-model="content" />
                <div v-else>{{ content }}</div>
            </div>
        </v-sheet>

        <v-sheet class="docItems">
            <div>
                <h1>helo</h1>
            </div>
        </v-sheet>
    </v-sheet>
</template>

<script>
import TipTapEditor from '~/components/TipTapEditor.vue';
import { useFetch } from '#app';

export default {
    data: () => ({
        open: ['Users'],
        items: [
            { title: 'Dashboard', disabled: false, href: 'breadcrumbs_dashboard' },
            { title: 'Link 1', disabled: false, href: 'breadcrumbs_link_1' },
            { title: 'Link 2', disabled: true, href: 'breadcrumbs_link_2' },
        ],
        isEditing: false,
        content: '', // Start with empty content
    }),
    methods: {
        async fetchContent() {
            const { data, error } = await useFetch('http://localhost:8000/api/docs/1/'); // Replace with your backend API endpoint
            if (error.value) {
                console.error('Failed to fetch content:', error.value);
            } else {
                this.content = data.value.content;
            }
        },
        async toggleEdit() {
            if (this.isEditing) {
                const { error } = await useFetch('http://localhost:8000/api/docs/1/', {
                    method: 'POST',
                    body: { content: this.content },
                }); // Replace with your backend API endpoint
                if (error.value) {
                    console.error('Failed to save content:', error.value);
                } else {
                    console.log('Content saved successfully.');
                }
            }
            this.isEditing = !this.isEditing;
        },
    },
    mounted() {
        this.fetchContent();
    },
};
</script>

<style scoped>
.area {
    display: flex;
    margin-left: 4px;
    height: 100%;
    width: 100%;
}

.edit-btn {
    position: fixed;
    top: 500px;
    right: 200px;
    z-index: 1;
}

.sidebar {
    font-family: Binance PLEX;
}

.sidebar-list {
    width: 259px;
    height: 100%;
    font-family: Binance PLEX;
}

.sidebar-item:hover {
    color: #F0B90B;
    text-decoration: none;
    cursor: pointer;
}

.v-list-item {
    margin-top: 4px;
}

.v-list-item:hover {
    color: #F0B90B;
    text-decoration: none;
    cursor: pointer;
}

.content {
    min-width: 60%;
}

.breadcrumbs {
    margin-left: 8px;
    margin-top: 4px;
    font-family: Binance PLEX;
}

.doc {
    width: 800px;
    height: 100%;
    padding: 10px;
    font-family: Binance PLEX;
    background-color: rgb(245, 106, 113);
}

.docItems {
    width: 185px;
    height: 100%;
    margin-right: 4px;
    font-family: Binance PLEX;
    background-color: aqua;
}
</style>
