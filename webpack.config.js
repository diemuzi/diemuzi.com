const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const RemovePlugin = require('remove-files-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');

let path = require('path');
let webpack = require('webpack');

module.exports = {
    cache: true,
    devtool: false,
    entry: {
        'vendor': [
            'jquery',
            'popper.js',
            'bootstrap',
            '@fortawesome/fontawesome-free',
            'blockui-npm',
            'pwstrength-bootstrap',
            'datatables.net-bs4',
            'datatables.net-buttons-bs4',
            'datatables.net-responsive-bs4',
            'datatables.net-scroller-bs4',
            'datatables.net-select-bs4'
        ],
        'vendor-css': [
            'bootstrap/dist/css/bootstrap.css',
            '@fortawesome/fontawesome-free/css/all.css',
            'datatables.net-bs4/css/dataTables.bootstrap4.css',
            'datatables.net-buttons-bs4/css/buttons.bootstrap4.css',
            'datatables.net-responsive-bs4/css/responsive.bootstrap4.css',
            'datatables.net-scroller-bs4/css/scroller.bootstrap4.css',
            'datatables.net-select-bs4/css/select.bootstrap4.css'
        ]
    },
    mode: 'production',
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader
                    },
                    'css-loader'
                ]
            },
            {
                test: /\.(png|jpg|gif|ico)$/,
                loader: 'file-loader',
                options: {
                    name: 'images/[name].[ext]'
                }
            },
            {
                test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: 'url-loader?limit=10000&mimetype=application/font-woff'
            },
            {
                test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: 'file-loader',
                options: {
                    name: 'fonts/[name].[ext]'
                }
            }
        ]
    },
    output: {
        filename: '[name].js',
        chunkFilename: '[name].chunk.js',
        path: path.resolve(__dirname, 'diemuzi/static/webpack')
    },
    optimization: {
        minimize: true,
        minimizer: [
            new OptimizeCSSAssetsPlugin({}),
            new TerserPlugin({
                cache: true,
                parallel: true,
                sourceMap: false
            })
        ],
        splitChunks: {
            chunks: 'async',
            minSize: 30000,
            maxSize: 0,
            minChunks: 1,
            maxAsyncRequests: 5,
            maxInitialRequests: 3,
            automaticNameDelimiter: '~',
            name: true,
            cacheGroups: {
                vendors: {
                    test: /[\\/]node_modules[\\/]/,
                    priority: -10
                },
                commons: {
                    name: 'common',
                    chunks: 'initial',
                    minChunks: 2
                },
                default: {
                    minChunks: 2,
                    priority: -20,
                    reuseExistingChunk: true
                }
            }
        },
        removeEmptyChunks: true,
        mergeDuplicateChunks: true
    },
    performance: {
        hints: false,
        assetFilter: function (assetFilename) {
            return assetFilename.endsWith('.js');
        }
    },
    plugins: [
        //new CleanWebpackPlugin(['diemuzi/static', 'diemuzi/static/webpack']),
        new CleanWebpackPlugin({
            dry: false,
            verbose: true,
            cleanOnceBeforeBuildPatterns: ['**/*', '../*'],
            //cleanAfterEveryBuildPatterns: ['**/*', '../*'],
            dangerouslyAllowCleanPatternsOutsideProject: true
        }),
        new CopyWebpackPlugin([
            {
                from: '@ckeditor/ckeditor5-build-classic/build/ckeditor.js',
                to: path.resolve(__dirname, 'diemuzi/static/webpack'),
                context: 'node_modules'
            }
        ]),
        new MiniCssExtractPlugin({
            filename: '[name].css',
            chunkFilename: '[name].chunk.css'
        }),
        new RemovePlugin({
            after: {
                root: path.resolve(__dirname, 'diemuzi/static/webpack'),
                include: ['vendor-css.js']
            }
        }),
        new webpack.IgnorePlugin(/jsdom$/)
    ],
    resolve: {
        alias: {
            'jquery': 'jquery/src/jquery',
            'pwstrength-bootstrap': 'pwstrength-bootstrap/dist/pwstrength-bootstrap'
        }
    }
};