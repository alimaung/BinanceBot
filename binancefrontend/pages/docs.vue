<template>
    <v-card
        class="align-right"
        width="259"
        height="100%"
        >
        <v-list v-model:opened="open">
            <v-list-item title="Documentation"></v-list-item>

            <v-list-group value="Users">
                <template v-slot:activator="{ props }">
                    <v-list-item
                        v-bind="props"
                        prepend-icon="mdi-account-circle"
                        title="Users"
                    ></v-list-item>
                </template>

                <v-list-group value="Admin">
                    <template v-slot:activator="{ props }">
                        <v-list-item
                        v-bind="props"
                        title="Admin"
                        ></v-list-item>
                    </template>

                    <v-list-item
                        v-for="([title, icon], i) in admins"
                        :key="i"
                        :prepend-icon="icon"
                        :title="title"
                        :value="title"
                    ></v-list-item>
                </v-list-group>

                <v-list-group value="Actions">
                    <template v-slot:activator="{ props }">
                        <v-list-item
                        v-bind="props"
                        title="Actions"
                        ></v-list-item>
                    </template>

                    <v-list-item
                        v-for="([title, icon], i) in cruds"
                        :key="i"
                        :prepend-icon="icon"
                        :title="title"
                        :value="title"
                    ></v-list-item>
                </v-list-group>
            </v-list-group>
        </v-list>
    </v-card>

    <v-card>

    </v-card>
</template>


<script>
  export default {
    data: () => ({
      open: ['Users'],
      admins: [
        ['Management', 'mdi-account-multiple-outline'],
        ['Settings', 'mdi-cog-outline'],
      ],
      cruds: [
        ['Create', 'mdi-plus-outline'],
        ['Read', 'mdi-file-outline'],
        ['Update', 'mdi-update'],
        ['Delete', 'mdi-delete'],
      ],
    }),
  }
</script>

<style scoped>


</style>