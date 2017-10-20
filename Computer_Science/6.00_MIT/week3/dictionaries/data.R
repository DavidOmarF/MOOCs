# Incluír librería
library(ggplot2)

## Import data
rec_df <- read.csv(file = "./rec_stats.csv", header = FALSE, sep = ",")
# dict_df <- read.csv(file = "./dict_stats.csv", header = FALSE, sep = ",")

names(rec_df) = c("n", "calls", "time")
# names(dict_df) = c("n", "calls", "time")

# Escribir pdf, y definir el tamaño de la hoja
pdf("comparison.pdf", width=4, height=4)

# Crear primer gráfico
# rec_plot = ggplot(head(rec_df,30), aes(x=n, y=time)) +
#             geom_area()

# rec_plot_time = ggplot(dict_df, aes(x=n, y=time)) +
#             geom_area()

rec_plot_calls = ggplot(head(rec_df, 20), aes(x=n, y=calls)) +
            geom_area()
# Imprimir primer gráfico

# plot(rec_plot)
# plot(dict_plot)
plot(rec_plot_calls)


# dict_plot_time = ggplot(dict_df, aes(x=n, y=time)) +
#             geom_area()

# dict_plot_calls = ggplot(dict_df, aes(x=n, y=calls)) +
#             geom_area()
ggsave("comparison.png")
# Imprimir primer gráfico
# plot(rec_plot)
# plot(dict_plot)
# plot(dict_plot_calls)